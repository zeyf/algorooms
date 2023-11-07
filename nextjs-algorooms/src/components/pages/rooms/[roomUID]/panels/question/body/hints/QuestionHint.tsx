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
            <button className="hover:bg-gray-600" onClick={() => setShowHint(!showHint)}>
                { `Hint ${oneIndexing}` }
            </button>


            {
                showHint &&
                <div className="p-2 bg-black/30 m-2 rounded-lg">{ questionHint }</div>
            }

        </section>
    );

};
