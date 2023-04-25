// Module imports
import React from "react";


// Interface imports
import { codePanelInterface } from "./Interfaces";
import CodeEditor from "./CodeEditor";
import Header from "./header/Header";

export default ({
    uid
}:codePanelInterface) => {

    // Code

    return (
        <section>
            <Header />
            <CodeEditor uid={uid} />
        </section>
    );

};