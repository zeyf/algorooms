// Imports
import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import { createServer } from "http"
import { Server } from "socket.io";
import bodyParser from 'body-parser';
import { instrument } from '@socket.io/admin-ui';

import UserRoutes from "./routes/User";
import RoomRoutes from "./routes/Room";
import QuestionRoutes from "./routes/Question";


// Initialization
const app = express();


app.use(express.json());
app.use(bodyParser.urlencoded({ extended : true }));


const httpServer = createServer(app);
const io = new Server(httpServer, {
    cors: {
        origin: "http://localhost:3000",
        methods: [
            "GET",
            "POST"
        ]
    }
});



io.on("connection", (socket) => {

    socket.on("joinRoom", (room, socketUser) => {
        socket.join(room);
        console.log(`User Connected: ${socket.id}`);

        socket.broadcast.to(room).emit("members", { message: (() => `${socketUser} joined!`)(), username: socketUser } );
    });

    // socket.on("leftRoom", (messageCallback, room, socketUser) => {
    //     console.log(messageCallback(socketUser), room);
    //     socket.broadcast.to(room).emit("members", { message: messageCallback(socketUser), username: socketUser });
    // });

    socket.on("codeChange", (code, room) => {
        socket.broadcast.to(room).emit("updateEditor", code);
    });

    socket.on("backendLanguageChange", (language, room, socketUser) => {
        socket.broadcast.to(room).emit("frontendLanguageChange", language, socketUser);
    });

    socket.on("newChatMessage", (messageData, room) => {
        socket.broadcast.to(room).emit("updateTextChat", messageData);
    });

    socket.on("disconnect", () => {
       console.log(`User Disconnected: ${socket.id}`);
    });
})


app.use("/api/users", UserRoutes);
app.use("/api/rooms", RoomRoutes);
app.use("/api/questions", QuestionRoutes);



// middleware
app.use(cors());


// Connecting MongoDB
mongoose.connect("mongodb+srv://user:12345@algorooms.lau3kx4.mongodb.net/test?retryWrites=true&w=majority").then(() => {
    console.log("connected to database");
}).catch((err) => {
    console.log(err);
});





// Start server
httpServer.listen(4000, () => {
    console.log("Server is running");
});

