import express from "express";
import Room from "../models/RoomModel";
import createUID from "../utilities/createUID";
import {REQUEST_LOG, RESPONSE_LOG_AND_PASS} from "../utilities/log";
import Question from "../models/QuestionModel";
import shuffle from "../utilities/shuffle";
import axios from "axios";
import Submission from "../models/SubmissionModel";
import { CodeExecutionConstants, TestingConstants } from "../data/CONSTANTS";

const router = express.Router();
const ROUTE_BASE = "/api/rooms";

/*
*
* GET routes
*
* - /api/rooms/public
* - /api/rooms/verify/:roomUID
*
*****
*
* POST routes
*
* - /api/rooms/create
* - /api/rooms/update/:roomUID
* - /api/rooms/execute
*
*/

// Get a list of all public rooms
router.get("/public", async (req, res) => {

    // For logging and testing 
    REQUEST_LOG(ROUTE_BASE, req);

    // Find all rooms that have a public lobby access
    await Room.find({
        lobbyAccess: "Public"
    }).then((response) => {

        // Send response
        res.status(200).send(RESPONSE_LOG_AND_PASS({
            rooms: response
        }));

    });

});

// Checks if a room exists or not
router.get("/verify/:roomUID", async (req, res) => {

    // For logging and testing
    REQUEST_LOG(ROUTE_BASE, req);    

    // Extract the roomUID from the parameters
    const {
        params: {
            roomUID
        }
    } = req;

    // Check if a roomUID was not passed as parameter
    if (!roomUID) {

        // Send response with no existence
        res.status(200).send(RESPONSE_LOG_AND_PASS({
            exists: false
        }));

    } else {

        // Search for the single record of a room by it's UID
        await Room.findOne({
            uid: roomUID
        }).then((response) => {

            // Return whether or not it exists
            res.status(200).send(RESPONSE_LOG_AND_PASS({
                exists: response !== null,
                roomData: response
            }));

        });

    }


});

// Create the a room
router.post("/create", async (req, res) => {

    // For logging and testing
    REQUEST_LOG(ROUTE_BASE, req);

    // Destructure the body
    const {
        body: {
            name,
            capacity,
            topics,
            difficulty,
            lobbyAccess,
            host
        }
    } = req;

    // Create a room UID
    const uid = createUID();

    // Find questions by difficulty and searching for at least of the request body topics' in the topics field in a given record in the questions collection
    const questions = await Question.find({
        difficulty,
        topics: {
            "$in" : topics
        }
    }).then(response => {

        // Shuffle the response for pseudo-randomized ordering
        shuffle(response);

        return response.map(question => question.uid);
    });

    // Create the room's record in mongoDB
    await Room.create({
        name,
        capacity,
        topics,
        difficulty,
        lobbyAccess,
        uid,
        occupied: 0,
        host,
        questions
    }).then(response => {
        
        // Send response
        res.status(200).send(RESPONSE_LOG_AND_PASS({
            created: true,
            uid
        }));
    });

});

// Delete room from MongoDb
router.post("/delete", async (req, res) => {
    REQUEST_LOG(ROUTE_BASE, req);
    const {
        body: {
            roomUID
        }
    } = req

    console.log("delete: ", roomUID)
})

router.post("/update/usercount", async(req, res) => {

    // for logging and testing
    REQUEST_LOG(ROUTE_BASE, req);
    const {
        body: {
            roomUID
        }
    } = req

    const LIVEBLOCKS_API_KEY = "sk_dev_zrV3LKJ7TVlPZagOoN514nqbxy2BIUXOOu6Yej6bIhy5zq6U5MC1VyfpSb9B9Ris";

    const numberOfUsersInRoom = await axios.get(
        `https://api.liveblocks.io/v2/rooms/${roomUID}/active_users`,
        {
            headers: {
                Authorization: `Bearer ${LIVEBLOCKS_API_KEY}`
            }
        }
    ).then(liveBlocksResponse => liveBlocksResponse.data.data.length);

    if (numberOfUsersInRoom > 0) {
        await Room.updateOne(
            { uid: roomUID },
            { occupied: numberOfUsersInRoom }
        );

        
    } else {
        await Room.deleteOne({
            uid: roomUID
        });

        try {
            await axios.delete(
                `https://api.liveblocks.io/v2/rooms/${roomUID}`,
                {
                    headers: {
                        Authorization: `Bearer ${LIVEBLOCKS_API_KEY}`
                    }
                }
            )
        }
        catch (err) {
            console.log(err)
        }
    }



   // console.log("update count: ", occupied)
})

router.post("/update/:roomUID", async (req, res) => {

    // for logging and testing
    REQUEST_LOG(ROUTE_BASE, req);

    const {
        params: {
            roomUID
        },
        body: {
            topics,
            lobbyAccess,
            difficulty
        }
    } = req;

    await Room.findOneAndUpdate({
        uid: roomUID
    }, {
        topics,
        lobbyAccess,
        difficulty
    });

    res.status(200).send(RESPONSE_LOG_AND_PASS({
        updated: true
    }));

});

router.post("/execute", async (req, res) => {

    // for logging and testing
    REQUEST_LOG(ROUTE_BASE, req);

    const {
        body
    } = req;

    const {
        username,
        questionUID,
        questionTitle,
        timestamp,
        language
    } = body;

    const question = await Question.findOne({
        uid: questionUID
    }).then(mongoResponse => mongoResponse);


    const {
        templates
    } = question;

    console.log(templates)

    const {
        testingTemplate,
        libraries,
        testCases
    } = templates[body.relativeLanguage];

    
    body.script = [
        libraries.join("\n"),
        body.script,
        testingTemplate
    ].join("\n");

    console.log(body.script)


    const executeResponse = await axios.post("https://api.jdoodle.com/v1/execute", body).then(r => {
        return r;
    }).then(r => r.data);

    const {
        output
    } = executeResponse;

    const uid = createUID(50);
    const outputTokens = output.split(TestingConstants.TEST_INJECTION_PLACEMENT_TERM_SWAP).filter(term => term !== "" && term !== "\n")

    if (output === null) {
        await Submission.create({
            result: CodeExecutionConstants.WRONG_ANSWER,
            questionTitle,
            username,
            questionUID,
            timestamp,
            language,
            code: body.script,
            uid
        }).then(mongoResponse => {

            res.status(200).send(RESPONSE_LOG_AND_PASS({
                created: true,
                result: {
                    state: CodeExecutionConstants.WRONG_ANSWER,
                    userOutput: outputTokens[1],
                    expectedOutput: testCases[0][1],
                    testCaseIndex: 0,
                    totalTestCases: testCases.length
                }
            }));

        });
    } else if (outputTokens.length === 0) {
        await Submission.create({
            result: CodeExecutionConstants.WRONG_ANSWER,
            questionTitle,
            username,
            questionUID,
            timestamp,
            language,
            code: body.script,
            uid
        }).then(mongoResponse => {

            res.status(200).send(RESPONSE_LOG_AND_PASS({
                created: true,
                result: {
                    state: CodeExecutionConstants.WRONG_ANSWER,
                    userOutput: outputTokens[1],
                    expectedOutput: testCases[0][1],
                    testCaseIndex: 0,
                    totalTestCases: testCases.length
                }
            }));

        });
    } else if (/^WRONGANSWER_[0-9]*$/.test(outputTokens[0])) {

        await Submission.create({
            result: CodeExecutionConstants.WRONG_ANSWER,
            questionTitle,
            username,
            questionUID,
            timestamp,
            language,
            code: body.script,
            uid
        }).then(mongoResponse => {
            const testCaseIndex = Number(outputTokens[0].split("_")[1])
            res.status(200).send(RESPONSE_LOG_AND_PASS({
                created: true,
                result: {
                    state: CodeExecutionConstants.WRONG_ANSWER,
                    userOutput: outputTokens[1],
                    expectedOutput: testCases[testCaseIndex][1],
                    testCaseIndex: testCaseIndex,
                    totalTestCases: testCases.length,
                }
            }));

        });

    // If wrong answer or other case...
    // Must be extended further to handle
    } else if (/^ACCEPTED$/.test(outputTokens[0])) {

        await Submission.create({
            result: CodeExecutionConstants.ACCEPTED,
            username,
            questionUID,
            questionTitle,
            timestamp,
            language,
            code: body.script,
            uid
        }).then(mongoResponse => {

            res.status(200).send(RESPONSE_LOG_AND_PASS({
                created: true,
                result: {
                    state: CodeExecutionConstants.ACCEPTED,
                    userOutput: outputTokens[1],
                    expectedOutput: outputTokens[1],
                    testCaseIndex: testCases.length - 1,
                    totalTestCases: testCases.length,
                }
            }));

        });

    } else {
        outputTokens[0] = outputTokens[0].replaceAll(/WRONGANSWER_[0-9]*$/gi, "").replaceAll(/ACCEPTED/gi, "")
        await Submission.create({
            result: CodeExecutionConstants.WRONG_ANSWER,
            username,
            questionUID,
            questionTitle,
            timestamp,
            language,
            code: body.script,
            uid
        }).then(mongoResponse => {

            res.status(200).send(RESPONSE_LOG_AND_PASS({
                created: true,
                result: {
                    state: CodeExecutionConstants.WRONG_ANSWER,
                    userOutput: outputTokens[0],
                    expectedOutput: testCases[0][1],
                    testCaseIndex: 0,
                    totalTestCases: testCases.length,
                }
            }));

        });
    }


});

export default router;