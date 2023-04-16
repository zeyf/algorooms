import express from "express";
import Question from "../models/QuestionModel";
import LOG from "../utilities/log";

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


    await Question.find({
        difficulty,
        topics: {
            "$in" : topics
        }
    }).then(response => {

        res.status(200).send({
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