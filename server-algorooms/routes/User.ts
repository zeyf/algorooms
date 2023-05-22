import express from "express";
import User from "../models/UserModel";
import LOG from "../utilities/log";
import Submission from "../models/SubmissionModel";

const router = express.Router();
const ROUTE_BASE = "/api/users";

/*
*
* GET routes
*
* - /api/users/verify/:profileUID
* - /api/users/verifyAuth/:authUID
*
*****
*
* POST routes
*
* - /api/users/create
*
*/

// This route is to check if user exists
router.get("/verify/:profileUID", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Extract the profileUID from the parameters
    const {
        params: {
            profileUID
        }
    } = req;

    // Check if there is a profileUID or not
    if (!profileUID) {
        
        // Sends response with no existence
        res.status(200).send({
            exists: false
        });

    } else {
        
        // Try to find a user with a given profileUID
        const foundUserResponse = await User.findOne({
            username: profileUID
        }).then(mongoResponse => mongoResponse);

        // Track whether the single record was found based on the username
        const exists = foundUserResponse !== null;
    
        // If the user does not exist
        if (!exists) {
            
            // Send response that nothing was found
            res.status(200).send({
                exists,
                profileData: foundUserResponse
            });

        // Otherwise if the user exists
        } else {

            // Pull the users' submissions
            const submissions = await Submission.find({
                username: profileUID
            }).then(mongoResponse => mongoResponse);

            // Inject the submissions to the user record in descending order by timestamp
            foundUserResponse["submissions"] = submissions.sort((a, b) => b.timestamp - a.timestamp);

            // Sends response with existence and data
            res.status(200).send({
                exists,
                profileData: foundUserResponse
            });

        }

    }

});

// This route is to check if user exists
router.get("/verifyAuth/:authUID", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Extract the profileUID from the parameters
    const {
        params: {
            authUID
        }
    } = req;

    // Check if there is a profileUID or not
    if (!authUID) {
        
        // Sends response with no existence
        res.status(200).send({
            exists: false
        });

    } else {
        
        // Try to find a user with a given profileUID
        await User.findOne({
            authuid: authUID
        }).then(response => {
            
            // Sends response with existence and data
            res.status(200).send({
                exists: response !== null,
                profileData: response
            });
            
        });
    }

});

// The assumption is that search will be attempted before create is utilized.
router.post("/create", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Extract the Auth0 authuid and desired username from the body
    const {
        body: {
            authuid,
            username,
            picture
        }
    } = req;

    // If either is undefined or ""
    if (!authuid || !username) {

        // Existence is not possible, send back this response
        res.status(200).send({
            exists: false
        });

    // Otherwise we have SOMETHING for both the authuid and username in the body
    } else {

        // Create a record of a user with the authuid, username, and a blank profile
        await User.create({
            authuid,
            username,
            picture,
            bestTopics: [],
            questionsSolved: {
                simpler: 0,
                simple: 0,
                notSimple: 0
            }
        }).then((mongoResponse) => {

            // Sends response with creation of the new record with the user's data
            res.status(200).send({
                created: true
            })

        });
    }

});

export default router;