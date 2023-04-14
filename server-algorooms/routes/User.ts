 import express from "express";
import User from "../models/UserModel";
import { IUser } from "../models/UserModel";

const router = express.Router();

// This route is to check if user exists
router.get("/verify/:profileUID", async (req, res) => {

    // For logging and testing
    const date = new Date();
    const hour = date.getHours(), minutes = date.getMinutes();
    console.log(`GET::/api/users/verify/:profileUID @ ${hour}:${minutes} ${hour < 12 ? "AM" : "PM"}`);

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
        await User.findOne({
            username: profileUID
        }).then((response) => {
            
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
    const date = new Date();
    const hour = date.getHours(), minutes = date.getMinutes();
    console.log(`POST::/api/users/create @ ${hour}:${minutes} ${hour < 12 ? "AM" : "PM"}`);

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