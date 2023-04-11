// Import statements
import React from "react";
import { questionHeaderInterface } from "./Interfaces";
import QuestionDifficultyRanking from "./QuestionDifficultyRanking";

export default ({
    questionIndex,
    questionTitle,
    questionDifficulty
}:questionHeaderInterface) => {

    return (
        <section className="px-2 py-4 w-full bg-main flex justify-between border-2 border-[red]">

            <section className="flex items-center">
                <h1 className="font-bold text-xl">
                    {`${questionIndex}. ${questionTitle}`}
                </h1>
            </section>

            <QuestionDifficultyRanking
                questionDifficulty={questionDifficulty}
            />
        </section>
    );

};
