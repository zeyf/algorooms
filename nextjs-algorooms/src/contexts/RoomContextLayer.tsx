import { useUser } from "@auth0/nextjs-auth0/client";
import { createContext, useEffect, useState } from "react";
import { roomContextLayerInterface } from "./Interfaces";
import { io } from "socket.io-client";
import axios from "axios";
import buildRoute from "@/utilities/buildRoute";

const socket = io('http://localhost:4000', {
    autoConnect: false
});

export const RoomContext = createContext<roomContextLayerInterface>({
    uid: "",
    socket,

    members: [  ],
    messages: [  ],
    language: "python",
    code: "def solution():\n\tprint('Hello World!')",
    runningCode: false,
    submittingCode: false,
    topics: [  ],
    difficulty: "",
    lobbyAccess: "",
});

export default ({
    children,
    uid,
    topics,
    difficulty,
    lobbyAccess
}:any) => {
    
    const [
        members,
        setMembers
    ] = useState<any[]>([  ]);

    const [
        messages,
        setMessages
    ] = useState<any[]>([  ]);

    const [
        language,
        setLanguage
    ] = useState<string>("python");

    const [
        code,
        setCode
    ] = useState<string>("def solution():\n\tprint('Hello World!')");

    const [
        runningCode,
        setRunningCode
    ] = useState(false);

    const [
        submittingCode,
        setSubmittingCode
    ] = useState(false);

    const [
        roomTopics,
        setTopics
    ] = useState<any[]>(topics);

    const [
        roomLobbyAccess,
        setLobbyAccess
    ] = useState<string>(lobbyAccess);

    const [
        roomDifficulty,
        setDifficulty
    ] = useState<string>(difficulty);

    return (
        <RoomContext.Provider
            value={{
                uid,
                socket,
                members,
                setMembers,
                messages,
                setMessages,
                language,
                setLanguage,
                code,
                setCode,
                runningCode,
                setRunningCode,
                submittingCode,
                setSubmittingCode,
                topics: roomTopics,
                setTopics,
                lobbyAccess: roomLobbyAccess,
                setLobbyAccess,
                difficulty: roomDifficulty,
                setDifficulty
            }}
        >
            { children }
        </RoomContext.Provider>
    );

};