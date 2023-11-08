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
        <section className="py-2">
            <p className="mb-2 font-bold">Topics</p>
            <div className="flex flex-row flex-wrap w-full">
              <div>
                {
                    // Display all question topics
                    questionTopics.map(
                        (topic: string) => <QuestionTopic questionTopic={ topic } />
                    )
                }
              </div>
            </div>

        </section>
    );

};
