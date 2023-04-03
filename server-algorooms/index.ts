// Imports
import express from 'express';
import mongoose from 'mongoose';
import { createServer } from "http"
import { Server } from "socket.io";


// Initialization
const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {

})

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
httpServer.listen(3001, () => {
    console.log("Server is running");
});

