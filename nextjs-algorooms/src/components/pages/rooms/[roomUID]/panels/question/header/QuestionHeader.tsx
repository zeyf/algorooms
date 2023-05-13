// Import statements
import React from "react";
import { questionHeaderInterface } from "./Interfaces";
import QuestionDifficultyRanking from "./QuestionDifficultyRanking";
import { useStorage } from "../../../../../../../../liveblocks.config";

export default ({


}) => {

    // Get the question title
    const questionTitle = useStorage(r => r.currentQuestion.title);

    // Get the question difficulty
    const questionDifficulty = useStorage(r => r.currentQuestion.difficulty);

    return (
        <section className="px-2 py-4 w-full bg-main flex justify-between border-b-2 ]">

            <section className="flex items-center">
                <h1 className="font-bold text-xl">
                    {`${questionTitle}`}
                </h1>
            </section>

            <QuestionDifficultyRanking
                questionDifficulty={questionDifficulty}
            />
        </section>
    );

};
