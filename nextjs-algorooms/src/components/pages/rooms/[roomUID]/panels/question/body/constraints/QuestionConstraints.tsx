// Module imports
import React from "react";

// Interface imports
import { questionConstraintsInterface } from "./Interfaces";

// Component imports
import Constraint from "./QuestionConstraint";

export default ({
    questionConstraints
}:questionConstraintsInterface) => {

    // Code

    return (
        <section>
            <span>Constraints</span>
            <br/>

            {
                questionConstraints.map(
                    (constraint: string) => <Constraint questionConstraint={ constraint } />
                )
            }
        </section>
    );

};
