import express, { response } from "express";
import Question from "../models/QuestionModel";
import LOG from "../utilities/log";
import shuffle from "../utilities/shuffle";
import createUID from "../utilities/createUID";

const router = express.Router();
const ROUTE_BASE = "/api/questions";

/*
*
* POST routes
*
* - /api/questions/create
* - /api/questions/filter
*
*/

router.get("/verify/:questionUID", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    const {
        params: {
            questionUID
        }
    } = req;

    await Question.findOne({
        uid: questionUID
    }).then(mongoResponse => {

        res.status(200).send({
            exists: mongoResponse !== null,
            question: mongoResponse
        });

    })

});

router.post("/filter", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Extract the body
    const {
        body: {
            difficulty,
            topics
        }
    } = req;

    // Find questions by difficulty and searching for at least of the request body topics' in the topics field in a given record in the questions collection
    await Question.find({
        difficulty,
        topics: {
            "$in" : topics
        }
    }).then(response => {

        // Shuffle the response for pseudo-randomized ordering
        shuffle(response);

        // Send the questions!
        res.status(200).send({
            exists: response.length > 0,
            questions: response.map(question => question.uid)
        });

    });

});

router.get("/approve", async (req, res) => {
    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Search for question with isApproved to be false
    await Question.find({
        isApproved: false
    }).then(response => {

        // Send the questions
        res.status(200).send({
            questions: response
        })
    })
})

router.post("/create", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Extract body data
    const {
        body: {
            title,
            difficulty,
            topics,
            description,
            constraints,
            hints,
            isApproved
        }
    } = req;

    const uid = createUID();

    await Question.create({
        title,
        uid,
        difficulty,
        topics,
        description,
        constraints,
        hints,
        isApproved
    }).then((response) => {

        res.status(200).send({
            created: true
        });

    })

});

export default router;