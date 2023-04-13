// Import statements
import React from "react";
import { questionDifficultyRankingInterface } from "./Interfaces";

export default ({
    questionDifficulty
}:questionDifficultyRankingInterface) => {

    // Sets the color for the background based on the question difficulty
    const setColor = ():string => {
        if (questionDifficulty === "Simpler")
            return "bg-[#90EE90]";
        else if (questionDifficulty === "Simple")
            return "bg-[#faf884]";
        else if (questionDifficulty === "Not Simple")
            return "bg-[#ff6961]";
        return "";
    };

    // Sets the color of the text based on the question difficulty
    const setTextColor = ():string => {
        if (questionDifficulty === "Simpler")
            return "text-[#006400]";
        else if (questionDifficulty === "Simple")
            return "text-[#FFFF00]";
        else if (questionDifficulty === "Not Simple")
            return "text-[#8B0000]";
        return "";
    };

    return (
        <section className={`${setColor()} rounded-xl ${setTextColor()} px-1 py-1 bg-opacity-75 drop-shadow-lg`}>
            { questionDifficulty }
        </section>
    );

};
