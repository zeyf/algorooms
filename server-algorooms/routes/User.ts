import express from "express";
import User from "../models/UserModel";

const router = express.Router();

router.get("/search/:profileUID", async (req, res) => {

    const {
        params: {
            profileUID
        }
    } = req;

    await User.find({
        nickname: profileUID
    }).then((response) => {
        console.log(response);
        res.send(response);
    });

});

export default router;