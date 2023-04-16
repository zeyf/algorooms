// Imports
import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import { createServer } from "http"
import { Server } from "socket.io";
import bodyParser from 'body-parser';

import UserRoutes from "./routes/User";
import RoomRoutes from "./routes/Room";
import QuestionRoutes from "./routes/Question";


// Initialization
const app = express();

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended : true }));

app.use("/api/users", UserRoutes);
app.use("/api/rooms", RoomRoutes);
app.use("/api/questions", QuestionRoutes);

const httpServer = createServer(app);
const io = new Server(httpServer, {
    cors: {
        origin: "https://localhost:4000",
        methods: ["GET", "POST"]
    }
});

// middleware
app.use(cors());


// Connecting MongoDB
mongoose.connect("mongodb+srv://user:12345@algorooms.lau3kx4.mongodb.net/test?retryWrites=true&w=majority").then(() => {
    console.log("connected to database");
}).catch((err) => {
    console.log(err);
});

io.on("connection", (socket) => {
    console.log(`User Connected: ${socket.id}`)
    
    socket.on("joinRoom", (arg) => {
        console.log("RoomUID: ", arg)
    })

    socket.on("disconnect", () => {
        console.log("User Disconnected", socket.id)
    })
})

// Start server
httpServer.listen(4000, () => {
    console.log("Server is running");
});

