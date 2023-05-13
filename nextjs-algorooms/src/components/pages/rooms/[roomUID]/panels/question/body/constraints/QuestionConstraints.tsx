// Module imports
import React from "react";

// Interface imports
import { questionConstraintsInterface } from "./Interfaces";

// Component imports
import Constraint from "./QuestionConstraint";
import { useStorage } from "../../../../../../../../../liveblocks.config";

export default ({

}) => {

    // Get the question constraints
    const questionConstraints = useStorage(r => r.currentQuestion.constraints);

    return (
        <section>
            <span>Constraints</span>
            <br/>

            {
                // Display all question constraints

                questionConstraints.map(
                    (constraint: string) => <Constraint questionConstraint={ constraint } />
                )
            }
        </section>
    );

};
