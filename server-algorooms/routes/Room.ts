import express from "express";
import Room from "../models/RoomModel";
import createUID from "../utilities/createUID";

const router = express.Router();




router.post("/create", async (req, res) => {

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

    await Room.create({
        capacity,
        lobbyAccess,
        topics,
        difficulty,
        name,
        uid
    }).then((response) => {
        console.log(`Created Room:\n\nUID: ${uid}\nName: ${name}\nTopics: ${topics}\n`);

        // createWebSocket()
        res.status(200).send({
            created: true
        });
    });

});

router.get("/publicRooms", async (req, res) => {

    await Room.find({
        lobbyAccess: "Public"
    }).then((response) => {
        
        const exists = response.length > 0;

        res.status(200).send({
            exists,
            rooms: response
        });

    });

});




export default router;