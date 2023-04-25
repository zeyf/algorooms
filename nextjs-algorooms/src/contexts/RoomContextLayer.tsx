import { useUser } from "@auth0/nextjs-auth0/client";
import { createContext, useState } from "react";
import { roomContextLayerInterface } from "./Interfaces";
import { io } from "socket.io-client";

const socket = io('http://localhost:4000', {
    autoConnect: false
});

export const RoomContext = createContext<roomContextLayerInterface>({
    uid: "",
    members: [  ],
    messages: [  ],
    language: "python",
    code: "def solution():\n\tprint('Hello World!')",
    socket
});

export default ({
    children,
    uid
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
    ] = useState<string>("");

    return (
        <RoomContext.Provider
            value={{
                uid,
                members,
                setMembers,
                messages,
                setMessages,
                language,
                setLanguage,
                code,
                setCode,
                socket
            }}
        >
            { children }
        </RoomContext.Provider>
    );

};