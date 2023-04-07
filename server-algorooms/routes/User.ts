 import express from "express";
import User from "../models/UserModel";

const router = express.Router();

// This route is specifically used for verification of a profileUID (that is user selected)
router.get("/search/:profileUID", async (req, res) => {
    
    // Extract the parameters
    const {
        params: {
            profileUID
        }
    } = req;


    // If undefined or ""
    if (!profileUID) {

        // Existence is not possible, send back this response
        res.status(200).send({
            exists: false
        });
    
    // Otherwise we have SOMETHING being parameterized as profileUID
    } else {

        // Try finding a record with the username in the user namespace
        await User.find({
            username: profileUID
        }).then((mongoResponse) => {

            // Stores if we have found a user with this username
            const exists = mongoResponse.length > 0;
            
            // Sends response with existence of profileUID parameter
            res.status(200).send({
                exists
            });

        });
    }

});


// The assumption is that search will be attempted before create is utilized.
router.post("/create", async (req, res) => {

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