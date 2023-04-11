import { useUser } from "@auth0/nextjs-auth0/client";
import { createContext } from "react";
import { roomContextLayerInterface } from "./Interfaces";

export const RoomContext = createContext<roomContextLayerInterface>({

});

export default ({
    children
}:any) => (
    <RoomContext.Provider
        value={{
            
        }}
    >
        { children }
    </RoomContext.Provider>
);