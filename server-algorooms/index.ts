// Imports
import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import { createServer } from "http"
import { Server } from "socket.io";
import bodyParser from 'body-parser';

import UserRoutes from "./routes/User";

// Initialization
const app = express();

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended : true }));

app.use("/api/user", UserRoutes);

const httpServer = createServer(app);
const io = new Server(httpServer, {

})

// middleware
app.use(cors());


// Connecting MongoDB
mongoose.connect("mongodb+srv://user:12345@algorooms.lau3kx4.mongodb.net/test?retryWrites=true&w=majority").then(() => {
    console.log("connected to database")
}).catch((err) => {
    console.log(err)
})

io.on("connection", (socket) => {
    console.log(`User Connected: ${socket.id}`)
    
    socket.on("disconnect", () => {
        console.log("User Disconnected", socket.id)
    })
})

// Start server
httpServer.listen(4000, () => {
    console.log("Server is running");
});

