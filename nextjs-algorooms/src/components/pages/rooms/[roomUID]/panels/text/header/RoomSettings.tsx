// Module imports
import React, { useState } from "react";

// Interface imports
import { roomSettingsInterface } from "./Interfaces";

export default ({
    topics,
    difficulty,
    link
}:roomSettingsInterface) => {

    // State handlers
    const [ settingsModalIsOpen, setSettingsModalIsOpen ] = useState<boolean>(false);

    // Code

    return (
        <section>
            {/* Body */}
        </section>
    );

};
