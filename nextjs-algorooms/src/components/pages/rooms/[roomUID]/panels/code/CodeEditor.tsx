// Module imports
import React, { useContext } from "react";
import CodeMirror from '@uiw/react-codemirror';
import { javascript as JAVASCRIPT_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-javascript';
import { python as PYTHON_SYNTAX_HIGHLIGHTING_EXTENSION } from "@codemirror/lang-python";
import { cpp as CPP_SYNTAX_HIGHLIGHTING_EXTENSION } from "@codemirror/lang-cpp";
import { java as JAVA_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-java';

import { darcula } from '@uiw/codemirror-theme-darcula'
import { sublime } from '@uiw/codemirror-theme-sublime'
import { Select, Option } from "@material-tailwind/react";
import { Button } from "flowbite-react";
import { useState, useRef, useEffect } from 'react'

// Interface imports
import { codeEditorInterface } from "./Interfaces";
import { countReset } from "console";
import rooms from "@/pages/rooms";
import { RoomContext } from "@/contexts/RoomContextLayer";

export default ({
uid
}:codeEditorInterface) => {

    const {
        code,
        setCode,
        socket,
        language
    } = useContext(RoomContext);

    const languageMapping = [
        [ "python", PYTHON_SYNTAX_HIGHLIGHTING_EXTENSION ],
        [ "javascript", JAVASCRIPT_SYNTAX_HIGHLIGHTING_EXTENSION ],
        [ "cpp", CPP_SYNTAX_HIGHLIGHTING_EXTENSION ],
        [ "java", JAVA_SYNTAX_HIGHLIGHTING_EXTENSION ]
    ];

    // Code
    const onChange = React.useCallback((value:any, viewUpdate:any) => {
        socket.emit("codeChange", value, uid);
        socket.on("updateEditor", (arg:any) => {
            setCode(arg);
        });
    }, [  ]);


    return (
        <div className="w-[822px] h-[649px]">
            <div className="rounded-lg overflow-hidden w-[822px] h-[579px] mt-5">
                <CodeMirror
                    value = {code}
                    onChange={onChange}
                    height="579px"
                    width="822px"
                    extensions={
                        languageMapping
                        .filter(([ lang, ext ]:any[]) => language === lang)
                        .map(([ lang, ext ]:any[]) => ext())
                    }
                    theme={sublime}
                />
            </div>

        </div>
    );

};
