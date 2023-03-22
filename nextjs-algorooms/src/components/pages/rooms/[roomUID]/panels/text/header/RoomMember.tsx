// Module imports
import React from "react";

// Interface imports
import { roomMemberInterface } from "./Interfaces";

export default ({
    member
}:roomMemberInterface) => {

    // Code

    return (
        <section>
            { member }
        </section>
    );

};
