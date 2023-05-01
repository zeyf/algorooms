import express from "express";
import Announcement from "../models/AnnouncementModel";
import LOG from "../utilities/log";
import shuffle from "../utilities/shuffle";
import createUID from "../utilities/createUID";

const router = express.Router();
const ROUTE_BASE = "/api/announcements";

/*
*
* GET routes
*
* - /api/announcements/verify/:announcementID
* - /api/announcements/all
*
*****
*
* POST routes
*
* - /api/announcements/create
*
*/

router.post("/create", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Extract the body
    const {
        body: {
            title,
            message,
            by
        }
    } = req;

    const uid = createUID();

    await Announcement.create({
        title,
        message,
        by,
        timestamp: Date.now(),
        uid
    }).then(mongoResponse => {

        res.status(200).send({
            created: true,
            uid
        });

    });

});

router.get("/verify/:announcementUID", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    // Extract body data
    const {
        params: {
            announcementUID
        }
    } = req;

    await Announcement.findOne({
        uid: announcementUID
    }).then(mongoResponse => {

        res.status(200).send({
            exists: mongoResponse !== null,
            announcement: mongoResponse
        });

    });

});

router.get("/all", async (req, res) => {

    // For logging and testing
    LOG(ROUTE_BASE, req);

    await Announcement.find({

    }).then(mongoResponse => {

        const exists = mongoResponse.length > 0;

        res.status(200).send({
            exists,
            announcements: mongoResponse
        });

    });

});

export default router;