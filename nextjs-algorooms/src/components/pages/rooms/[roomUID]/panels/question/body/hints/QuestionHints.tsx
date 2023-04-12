// Module imports
import React from "react";

// Interface imports
import { questionHintsInterface } from "./Interfaces";

// Component imports
import Hint from "./QuestionHint";

export default ({
    questionHints
}:questionHintsInterface) => {

    return (
        <section>
            <p>Hints</p>
            <br/>

            {
                questionHints.map(
                    (hint: string, index: number) => <Hint questionHint={ hint } questionHintIndex={ index } />
                )
            }

        </section>
    );

};
