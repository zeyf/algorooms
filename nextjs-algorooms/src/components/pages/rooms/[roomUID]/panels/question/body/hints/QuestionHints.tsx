// Module imports
import React from "react";

// Interface imports
import { questionHintsInterface } from "./Interfaces";

// Component imports
import Hint from "./QuestionHint";
import { useStorage } from "../../../../../../../../../liveblocks.config";

export default ({

}) => {

    // Get the question hints
    const questionHints = useStorage(r => r.currentQuestion.hints);

    return (
        <section>
            <p>Hints</p>
            <br/>

            {
                // Display all question hints

                questionHints.map(
                    (hint: string, index: number) => <Hint questionHint={ hint } questionHintIndex={ index } />
                )
            }

        </section>
    );

};
