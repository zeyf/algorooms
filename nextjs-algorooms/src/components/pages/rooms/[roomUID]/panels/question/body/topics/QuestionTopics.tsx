// Module imports
import React from "react";

// Interface imports
import { questionTopicsInterface } from "./Interfaces";

// Component imports
import QuestionTopic from "./QuestionTopic";
import { useStorage } from "../../../../../../../../../liveblocks.config";

export default ({

}) => {

    // Get the question topics
    const questionTopics = useStorage(r => r.currentQuestion.topics);

    return (
        <section>
            <p>Topics</p>
            <br/>
            
            {
                // Display all question topics

                questionTopics.map(
                    (topic: string) => <QuestionTopic questionTopic={ topic } />
                )
            }

        </section>
    );

};
