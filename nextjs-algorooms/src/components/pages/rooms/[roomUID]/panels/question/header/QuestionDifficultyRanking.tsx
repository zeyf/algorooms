// Import statements
import React from "react";
import { questionDifficultyRankingInterface } from "./Interfaces";

export default ({
    questionDifficulty
}:questionDifficultyRankingInterface) => {

    // Sets the color for the background based on the question difficulty
    const setBackgroundColor = ():string => {
        if (questionDifficulty === "Easy")
            return "bg-[#90EE90]";
        else if (questionDifficulty === "Medium")
            return "bg-[#faf884]";
        else if (questionDifficulty === "Hard")
            return "bg-[#ff6961]";
        return "";
    };

    // Sets the color of the text based on the question difficulty
    const setTextColor = ():string => {
        if (questionDifficulty === "Easy")
            return "text-[#006400]";
        else if (questionDifficulty === "Medium")
            return "text-[#FFFF00]";
        else if (questionDifficulty === "Not Hard")
            return "text-[#8B0000]";
        return "";
    };

    return (
        <section className={`${setBackgroundColor()} rounded-xl ${setTextColor()} px-1 py-1 bg-opacity-75 drop-shadow-lg`}>
            { questionDifficulty }
        </section>
    );

};
