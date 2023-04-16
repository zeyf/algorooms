import express from "express";
import Question from "../models/QuestionModel";
import LOG from "../utilities/log";
import shuffle from "../utilities/shuffle";

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
            questions: response
        });

    });

});

router.post("/create", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Extract body data
    const {
        body: {
            title,
            index,
            difficulty,
            topics,
            description,
            constraints,
            hints
        }
    } = req;

    await Question.create({
        title,
        index,
        difficulty,
        topics,
        description,
        constraints,
        hints
    }).then((response) => {

        res.status(200).send({
            created: true
        });

    })

});

export default router;