 import express from "express";
import User from "../models/UserModel";
import { IUser } from "../models/UserModel";

const router = express.Router();

// This route is specifically used for verification of a profileUID (that is user selected)
router.post("/search/:profileUID", async (req, res) => {
    
    // Extract the parameters
    const {
        params: {
            profileUID
        },
        body: {
            source
        }
    } = req;

    const profilePagePathRegex = /\/profile\/[0-9a-zA-Z]{1,}/,
          firstTimeUserPagePathRegex = /\/firsttimeuser/;
    
    const sourceIsDynamicProfile = profilePagePathRegex.test(source);
    const sourceIsFirstTimeUser = firstTimeUserPagePathRegex.test(source);


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

            const exists = mongoResponse["_doc" as any] !== undefined;

            if (sourceIsFirstTimeUser) {

                if (exists) {
                    console.log(`${profileUID} is a new user.`);
                }
                res.status(200).send({
                    exists
                });

            } else if (sourceIsDynamicProfile) {

                let mongoResponseCopy:any = {  };

                if (exists) {
                    mongoResponseCopy = { ...mongoResponse["_doc" as any] };
                    delete mongoResponseCopy["authuid"];
                }
                    
                res.status(200).send({
                    exists,
                    profileData: mongoResponseCopy
                });

            }
            
            // Sends response with existence of profileUID parameter

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