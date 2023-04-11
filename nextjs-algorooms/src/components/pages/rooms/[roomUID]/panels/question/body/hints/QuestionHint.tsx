// Module imports
import React, { useState } from "react";

// Interface imports
import { questionHintInterface } from "./Interfaces";

export default ({
    questionHint,
    questionHintIndex
}:questionHintInterface) => {

    // State handlers
    const [
        showHint,
        setShowHint
    ] = useState<boolean>(false);

    const oneIndexing = questionHintIndex + 1;

    return (
        <section>
            <span
                onClick={() => setShowHint(!showHint)}
            >
                { `Hint ${oneIndexing}` }
            </span>

            {
                showHint &&
                <span>{ questionHint }</span>
            }

        </section>
    );

};
