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
import rooms from "@/pages/rooms";

export default ({
socket,
uid
}:codeEditorInterface) => {

    // Code
    const onChange = React.useCallback((value:any, viewUpdate:any) => {
        socket.emit("codeChange", value, uid)
        socket.on("updateEditor", (arg:any) => {
            setCode(arg)
        })
    }, [] )

    const [code, setCode] = useState("hello")


    return (
        <div className="w-[822px] h-[649px]">
            <div className="rounded-lg overflow-hidden w-[822px] h-[579px] mt-5">
                <CodeMirror
                    value = {code}
                    onChange={onChange}
                    height="579px"
                    width="822px"
                    extensions={[javascript({ jsx: true })]}
                    theme={sublime}
                />
            </div>

        </div>
    );

};
