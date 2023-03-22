// Module imports
import React from "react";

// Interface imports
import { constraintsInterface } from "./Interfaces";

// Component imports
import Constraint from "./Constraint";

export default ({
    constraints
}:constraintsInterface) => {

    // Code

    return (
        <section>
            <span>Constraints</span>
            <br/>

            {
                constraints.map(
                    (constraint: string) => <Constraint constraint={ constraint } />
                )
            }
        </section>
    );

};
