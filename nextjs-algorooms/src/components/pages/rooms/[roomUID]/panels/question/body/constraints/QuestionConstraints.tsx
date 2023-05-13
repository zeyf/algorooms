// Module imports
import React from "react";

// Interface imports
import { questionConstraintsInterface } from "./Interfaces";

// Component imports
import Constraint from "./QuestionConstraint";
import { useStorage } from "../../../../../../../../../liveblocks.config";

export default ({

}) => {

    const questionConstraints = useStorage(r => r.currentQuestion.constraints);

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
