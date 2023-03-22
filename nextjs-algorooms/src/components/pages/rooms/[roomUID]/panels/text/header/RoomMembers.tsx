// Module imports
import React from "react";

// Interface imports
import { roomMembersInterface } from "./Interfaces";

// Component imports
import RoomMember from "./RoomMember";

export default ({
    members
}:roomMembersInterface) => {

    // Code

    return (
        <section>
            <span>Members</span>
            <br/>

            {
                members.map(
                    (member:string) => <RoomMember member={ member } />
                )
            }
        </section>
    );

};
