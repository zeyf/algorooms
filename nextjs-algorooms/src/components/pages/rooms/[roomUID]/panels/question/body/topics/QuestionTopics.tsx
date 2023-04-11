// Module imports
import React from "react";

// Interface imports
import { questionTopicsInterface } from "./Interfaces";

// Component imports
import QuestionTopic from "./QuestionTopic";

export default ({
    questionTopics
}:questionTopicsInterface) => {

    // Code

    return (
        <section>
            <p>Topics</p>
            <br/>
            
            {
                questionTopics.map(
                    (topic: string) => <QuestionTopic questionTopic={ topic } />
                )
            }

        </section>
    );

};
