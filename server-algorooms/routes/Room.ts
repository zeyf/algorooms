import express from "express";
import Room from "../models/RoomModel";
import createUID from "../utilities/createUID";

const router = express.Router();

// Create the a room
router.post("/create", async (req, res) => {

    // For logging and testing
    const date = new Date();
    const hour = date.getHours(), minutes = date.getMinutes();
    console.log(`POST::/api/rooms/create @ ${hour}:${minutes} ${hour <= 12 ? "AM" : "PM"}`);

    const {
        body: {
            capacity,
            lobbyAccess,
            topics,
            name,
            difficulty
        }
    } = req;

    // Create a room UID
    const uid = createUID();

    // Create the room's record in mongoDB
    await Room.create({
        capacity,
        lobbyAccess,
        topics,
        difficulty,
        name,
        uid
    }).then((response) => {
        // Send response
        res.status(200).send({
            created: true
        });
    });

});

// Get a list of all public rooms
router.get("/public", async (req, res) => {

    // For logging and testing
    const date = new Date();
    const hour = date.getHours(), minutes = date.getMinutes();
    console.log(`GET::/api/rooms/public @ ${hour}:${minutes} ${hour <= 12 ? "AM" : "PM"}`);

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
router.post("/verify", async (req, res) => {

        // For logging and testing
        const date = new Date();
        const hour = date.getHours(), minutes = date.getMinutes();
        console.log(`POST::/api/rooms/verify @ ${hour}:${minutes} ${hour <= 12 ? "AM" : "PM"}`);    

    const {
        body: {
            roomUID
        }
    } = req;

    // Search for the single record of a room by it's UID
    await Room.findOne({
        uid: roomUID
    }).then((response) => {

        // Return whether or not it exists
        res.status(200).send({
            exists: response !== null
        });

    });

});


export default router;