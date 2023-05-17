// Module imports
import React from "react";
import Header from "./header/Header";
import dynamic from "next/dynamic";
const CodeEditor = dynamic(() => import('./CodeEditor'), {ssr:false})
import Split from "react-split";
import CodeTester from "./CodeTester";



// Interface imports




export default ({

}) => {

    // Code

    return (
        <section>
            <Header />
            <Split direction="vertical" gutterSize={10} className="mt-2">
                <CodeEditor />
                <CodeTester />
            </Split>
        </section>
    );

};