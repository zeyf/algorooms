// Imports
import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import { createServer } from "http"
import { Server } from "socket.io";

// Initialization
const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
    cors:{
        origin: 'http://localhost:3000'
    }
})

io.on("connection", (socket) => {
    console.log(`User Connected: ${socket.id}`)
    
    socket.on("disconnect", () => {
        console.log("User Disconnected", socket.id)
    })
})

// Start server
httpServer.listen(3000, () => {
    console.log("Server is running");
});

