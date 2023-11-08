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
        <section className="pt-4 pb-2">
            <div className="font-bold">Hints</div>

            {
                // Display all question hints

                questionHints.map(
                    (hint: string, index: number) => <Hint questionHint={ hint } questionHintIndex={ index } />
                )
            }

        </section>
    );

};
