// Module imports
import React from "react";


// Interface imports
import { codePanelInterface } from "./Interfaces";
import CodeEditor from "./CodeEditor";
import Header from "./header/Header";

export default ({
    socket,
    uid
}:codePanelInterface) => {

    // Code

    return (
        <section>
            <Header />
            <CodeEditor socket={socket} uid={uid}/>
        </section>
    );

};