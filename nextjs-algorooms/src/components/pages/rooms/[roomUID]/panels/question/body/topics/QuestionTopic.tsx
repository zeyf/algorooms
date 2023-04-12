// Module imports
import React from "react";

// Interface imports
import { questionTopicInterface } from "./Interfaces";

export default ({
    questionTopic
}:questionTopicInterface) => {

    // Code

    return (
        <span>
            { questionTopic }
        </span>
    );

};
