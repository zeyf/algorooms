import { useUser } from "@auth0/nextjs-auth0/client";
import { createContext, useState } from "react";
import { roomContextLayerInterface } from "./Interfaces";

export const RoomContext = createContext<roomContextLayerInterface>({
    uid: "",
    members: [  ],
    messages: [  ]
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
                setMessages
            }}
        >
            { children }
        </RoomContext.Provider>
    );

};