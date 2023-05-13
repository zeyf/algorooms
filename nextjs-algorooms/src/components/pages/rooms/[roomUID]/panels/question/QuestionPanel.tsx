// Module imports
import React from "react";

// Interface imports
import { questionPanelInterface } from "./Interfaces";
import QuestionHeader from "./header/QuestionHeader";
import QuestionConstraints from "./body/constraints/QuestionConstraints";
import QuestionTopics from "./body/topics/QuestionTopics";
import QuestionHints from "./body/hints/QuestionHints";
import QuestionExamples from "./body/examples/QuestionExamples";
import { useStorage } from "../../../../../../../liveblocks.config";

export default ({

}) => {

    const questionBody = useStorage(r => r.currentQuestion.description);

    return (
        <div className="bg-darkAccent text-white">
            <QuestionHeader />
            <section className="px-2 py-4">
                <div className="whitespace-pre-line break-normal"> { questionBody } </div>
                
                <QuestionExamples />
                <QuestionHints />
                <QuestionTopics />
                <QuestionConstraints />
            </section>
        </div>
    );

};
