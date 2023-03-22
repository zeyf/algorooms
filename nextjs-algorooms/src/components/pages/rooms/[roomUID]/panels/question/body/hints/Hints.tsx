// Module imports
import React from "react";

// Interface imports
import { hintsInterface } from "./Interfaces";

// Component imports
import Hint from "./Hint";

export default ({
    hints
}:hintsInterface) => {

    // Code

    return (
        <section>
            <p>Hints</p>
            <br/>

            {
                hints.map(
                    (hint: string, index: number) => <Hint hint={ hint } index={ index } />
                )
            }

        </section>
    );

};
