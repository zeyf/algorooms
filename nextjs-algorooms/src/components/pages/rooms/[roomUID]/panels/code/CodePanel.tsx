// Module imports
import React from "react";
import Header from "./header/Header";
import dynamic from "next/dynamic";
import CodeTester from "./CodeTester";
const CodeEditor = dynamic(() => import('./CodeEditor'), {ssr:false})
import Split from 'react-split';



// Interface imports




export default ({

}) => {

    // Code

    return (
        <section className="w-full">
            <Header />
            <Split sizes={[70,30]} minSize={[300, 0]} direction="vertical" cursor="row-resize" className="w-full"
              style={{height: "calc(100% - 129px"}}
            >
              <div>
                <CodeEditor />
              </div>
              <div>
                <CodeTester />
              </div>
            </Split>
        </section>
    );

};