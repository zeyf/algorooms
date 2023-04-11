// Module imports
import React from "react";

// Interface imports
import { questionPanelInterface } from "./Interfaces";
import QuestionHeader from "./header/QuestionHeader";
import QuestionConstraints from "./body/constraints/QuestionConstraints";
import QuestionTopics from "./body/topics/QuestionTopics";
import QuestionHints from "./body/hints/QuestionHints";
import QuestionExamples from "./body/examples/QuestionExamples";

export default ({
    questionIndex,
    questionTitle,
    questionDifficulty,
    questionBody,
    questionExamples,
    questionConstraints,
    questionHints,
    questionTopics
}:questionPanelInterface) => {

    return (
        <section className="bg-darkAccent text-white overflow-y-hidden scrollbar scrollbar-thumb-white">
            <QuestionHeader
                questionIndex={questionIndex}
                questionTitle={questionTitle}
                questionDifficulty={questionDifficulty}
            />

            <section className="px-2 py-4">
                <span> { questionBody } </span>
                <QuestionExamples questionExamples={questionExamples} />
                <QuestionHints questionHints={questionHints} />
                <QuestionTopics questionTopics={questionTopics} />
                <QuestionConstraints questionConstraints={questionConstraints} />
            </section>
        </section>
    );

};
