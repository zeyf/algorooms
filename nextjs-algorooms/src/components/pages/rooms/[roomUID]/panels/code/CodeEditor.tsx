// Module imports
import React from "react";
import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { darcula } from '@uiw/codemirror-theme-darcula'
import { sublime } from '@uiw/codemirror-theme-sublime'
import { Select, Option } from "@material-tailwind/react";
import { Button } from "flowbite-react";
import { useState, useRef, useEffect } from 'react'

// Interface imports
import { codeEditorInterface } from "./Interfaces";
import { countReset } from "console";

export default ({

}:codeEditorInterface) => {

    let minutes = 15;
    let seconds = 0;
    const [[mins, secs], setTime] = useState([minutes, seconds])
    
    const tick = () => {
        if (mins === 0 && secs === 0){
            reset();
        }
        else if (secs === 0){
            setTime([mins - 1, 59]);
        }
        else{
            setTime([mins, secs-1]);
        }
    };

    useEffect(() => {
        const timerID = setInterval(() => tick(), 1000);
        return () => clearInterval(timerID);
    })

    const reset = () => setTime([minutes, seconds]);


    // Code
    const onChange = React.useCallback((value:any, viewUpdate:any) => {
        console.log('value:', value);
    }, [] )

    return (
        <div className="w-[822px] h-[649px]">
            <div className="w-[822px] flex flex-row space-x-5 items-center p-1">
                <div className="w-[200px]">
                    <Select label="Select Language" className="drop-shadow-lg" color="blue">
                        <Option>Python</Option>
                        <Option>Javascript</Option>
                    </Select>
                </div>

                <Button href="/" color="dark" className="drop-shadow-lg">Run</Button>
                <div className="text-white bg-[#051135] w-[95px] h-[46px] flex justify-center items-center rounded-xl drop-shadow-lg">
                    <h3 className="font-bold text-lg">
                        {`${mins.toString()} : ${secs.toString().padStart(2, '0')}`}
                    </h3>
                </div>
            </div>
            <div className="rounded-lg overflow-hidden w-[822px] h-[579px] mt-5">
                <CodeMirror
                    value = "console.log('hello world');"
                    height="579px"
                    width="822px"
                    extensions={[javascript({ jsx: true })]}
                    theme={sublime}
                />
            </div>

        </div>
    );

};
