// Module imports
import React from "react";
import Header from "./header/Header";
import dynamic from "next/dynamic";
const CodeEditor = dynamic(() => import('./CodeEditor'), {ssr:false})



// Interface imports




export default ({

}) => {

    // Code

    return (
        <section>
            <Header />
            <CodeEditor />
        </section>
    );

};