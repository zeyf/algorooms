// Module imports
import React from "react";

// Interface imports
import { topicsInterface } from "./Interfaces";

// Component imports
import Topic from "./Topic";

export default ({
    topics
}:topicsInterface) => {

    // Code

    return (
        <section>
            <p>Topics</p>
            <br/>
            
            {
                topics.map(
                    (topic: string) => <Topic topic={ topic } />
                )
            }

        </section>
    );

};
