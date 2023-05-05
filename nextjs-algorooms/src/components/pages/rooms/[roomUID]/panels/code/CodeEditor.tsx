// Module imports
import { useState, useRef, useEffect, useContext } from 'react'
import CodeMirror from '@uiw/react-codemirror';
import { javascript as JAVASCRIPT_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-javascript';
import { python as PYTHON_SYNTAX_HIGHLIGHTING_EXTENSION } from "@codemirror/lang-python";
import { cpp as CPP_SYNTAX_HIGHLIGHTING_EXTENSION } from "@codemirror/lang-cpp";
import { java as JAVA_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-java';
import { sublime } from '@uiw/codemirror-theme-sublime'
import * as Y from "yjs";
import { WebrtcProvider } from "y-webrtc";
import { yCollab } from 'y-codemirror.next'

// Interface imports
import { codeEditorInterface } from "./Interfaces";
import { countReset } from "console";
import rooms from "@/pages/rooms";
import { RoomContext } from "@/contexts/RoomContextLayer";
import { AppUserContext } from '@/contexts/AppUserContextLayer';

export default ({

}) => {

    const {
        socket,
        uid,
        code,
        setCode,
        language
    } = useContext(RoomContext);

    const {
        username
    } = useContext(AppUserContext);

    const languageMapping = [
        [ "python", PYTHON_SYNTAX_HIGHLIGHTING_EXTENSION ],
        [ "javascript", JAVASCRIPT_SYNTAX_HIGHLIGHTING_EXTENSION ],
        [ "cpp", CPP_SYNTAX_HIGHLIGHTING_EXTENSION ],
        [ "java", JAVA_SYNTAX_HIGHLIGHTING_EXTENSION ]
    ];

    // Code

    // const onChange = React.useCallback((value:any, viewUpdate:any) => {
    //     socket.emit("codeChange", value, uid);

    // }, [  ]);

    // socket.on("updateEditor", (arg:any) => {
    //     setCode(arg);
    // });

    const [collabRef, setCollabRef] = useState(null)

    useEffect(() => {
        const ydoc = new Y.Doc();
        const provider = new WebrtcProvider(uid, ydoc);
        const yText = ydoc.getText("codemirror");
        const awareness = provider.awareness;
        awareness.setLocalStateField("user", {
            name: username
        })
        const undoManager = new Y.UndoManager(yText);
        setCollabRef(yCollab(yText, awareness, {undoManager}))

        return () => {
            if (provider) {
                provider.disconnect();
                ydoc.destroy();
            }
        }
    }, [])
  

    return (
        <div className="w-[822px] h-[649px]">
            <div className="rounded-lg overflow-hidden w-[822px] h-[579px] mt-5">
                <CodeMirror
                    height="579px"
                    width="822px"
                    extensions={[
                        languageMapping
                        .filter(([ lang, ext ]:any[]) => language === lang)
                        .map(([ lang, ext ]:any[]) => ext()),
                        collabRef
                    ]
                    }
                    theme={sublime}
                />
            </div>

        </div>
    );

};
