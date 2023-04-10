// Import statements
import React from "react";
import CodeEditor from "@/components/pages/rooms/[roomUID]/panels/code/CodeEditor";

export default () => {  

    return (
        <div className="bg-[#222C4A] w-screen h-screen flex flex-row-reverse justify-center items-center">
            <div className="w-2/3 h-screen flex flex-col justify-center items-center">
                <CodeEditor />
            </div>
            <div className=" w-1/3 h-screen bg-black">
                Yo
            </div>
            
        </div>
    )
    

};

