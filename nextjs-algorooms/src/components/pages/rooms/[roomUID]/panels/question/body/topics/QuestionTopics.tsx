// Module imports
import React from "react";

// Interface imports
import { questionTopicsInterface } from "./Interfaces";

// Component imports
import QuestionTopic from "./QuestionTopic";
import { useStorage } from "../../../../../../../../../liveblocks.config";

export default ({

}) => {

    const questionTopics = useStorage(r => r.currentQuestion.topics);

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
