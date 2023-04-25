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

    return (
        <RoomContext.Provider
            value={{
                uid,
                members,
                setMembers,
                messages,
                setMessages,
                socket
            }}
        >
            { children }
        </RoomContext.Provider>
    );

};