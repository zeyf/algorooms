// Module imports
import React, { useState } from "react";

// Interface imports
import { hintInterface } from "./Interfaces";

export default ({
    hint,
    index
}:hintInterface) => {

    // State handlers
    const [ showHint, setShowHint ] = useState<boolean>(false);

    // Code
    const oneIndexing = index + 1;

    return (
        <section>
            <span
                onClick={() => setShowHint(!showHint)}
            >
                { `Hint ${oneIndexing}` }
            </span>

            {
                showHint &&
                <span>{ hint }</span>
            }

        </section>
    );

};
