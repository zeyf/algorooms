import express from "express";
import Room from "../models/RoomModel";
import createUID from "../utilities/createUID";
import LOG from "../utilities/log";
import Question from "../models/QuestionModel";
import shuffle from "../utilities/shuffle";
import axios from "axios";

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
    LOG(ROUTE_BASE, req);

    // Find all rooms that have a public lobby access
    await Room.find({
        lobbyAccess: "Public"
    }).then((response) => {

        // Send response
        res.status(200).send({
            rooms: response
        });

    });

});

// Checks if a room exists or not
router.get("/verify/:roomUID", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);    

    // Extract the roomUID from the parameters
    const {
        params: {
            roomUID
        }
    } = req;

    // Check if a roomUID was not passed as parameter
    if (!roomUID) {

        // Send response with no existence
        res.status(200).send({
            exists: false
        });

    } else {

        // Search for the single record of a room by it's UID
        await Room.findOne({
            uid: roomUID
        }).then((response) => {

            // Return whether or not it exists
            res.status(200).send({
                exists: response !== null,
                roomData: response
            });

        });

    }


});

// Create the a room
router.post("/create", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

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
        res.status(200).send({
            created: true,
            uid
        });
    });

});

router.post("/update/:roomUID", async (req, res) => {

    // for logging and testing
    LOG(ROUTE_BASE, req);

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

    res.status(200).send({
        updated: true
    });

});

router.post("/execute", async (req, res) => {

    // for logging and testing
    LOG(ROUTE_BASE, req);

    const {
        body
    } = req;

    const executeResponse = await axios.post("https://api.jdoodle.com/v1/execute", body).then(r => {
        return r;
    }).then(r => {

        const {
            output
        } = r.data;


        res.status(200).send({
            output
        });

    });


});

export default router;