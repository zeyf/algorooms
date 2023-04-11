// Import statements
import React from "react";
import { questionDifficultyRankingInterface } from "./Interfaces";

export default ({
    questionDifficulty
}:questionDifficultyRankingInterface) => {

    // Sets the color for the background based on the question difficulty
    const setColor = ():string => {
        if (questionDifficulty === "Simpler")
            return "bg-[#03fc73]";
        else if (questionDifficulty === "Simple")
            return "bg-[#fcf003]";
        else if (questionDifficulty === "Not Simple")
            return "bg-[#fc2403]";
        return "";
    };

    return (
        <section className={`${setColor()} border-2 border-[white] rounded-xl text-black px-4 py-2`}>
            { questionDifficulty }
        </section>
    );

};
