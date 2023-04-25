// Module imports
import React, { useContext, useEffect, useState } from "react";
import { Select, Option } from "@material-tailwind/react";
import { Button } from "flowbite-react";
import SettingsPop from "../../../shared/settingsPop";
import { FaCog } from "react-icons/fa";

// Interface imports
import { headerInterface } from "./Interfaces";
import CountdownTimer from "./CountdownTimer";
import { RoomContext } from "@/contexts/RoomContextLayer";
import { toast } from "react-toastify";
import { useUser } from "@auth0/nextjs-auth0/client";

export default ({

}:headerInterface) => {

    // Code
    const [
        isSettingsOpen,
        setIsSettingsOpen
    ] = useState(false);

    const [
        runningCode,
        setRunningCode
    ] = useState(false);

    const [
        submittingCode,
        setSubmittingCode
    ] = useState(false);

    const {
        language,
        setLanguage,
        socket,
        uid
    } = useContext(RoomContext);

    const {
        user
    } = useUser();

    useEffect(() => {
        socket.on("frontendLanguageChange", (language, socketUser) => {
            setLanguage(language);
        });

        socket.on("frontendCodeExecution", (message, socketUser) => {
            toast(message);
            setRunningCode(true);
            setSubmittingCode(true);

            setInterval(() => {
                setRunningCode(false);
                setSubmittingCode(false);
            }, 3000);
        });

    }, [  ]);

    const runCode = async () => {

    };

    return (
        <section>
            <div className="w-[822px] flex flex-row space-x-5 items-center p-1 justify-between">
                <div className="flex items-center gap-[21px]">
                    <div className="w-[200px]">
                        <select
                            // If you are the host, true. Otherwise, false.
                            disabled={runningCode || submittingCode}
                            placeholder="Select Language"
                            className="drop-shadow-lg"
                            color="blue"
                            defaultValue={language}
                            value={language}
                            onChange={e => {
                                socket.emit("backendLanguageChange", e.target.value, uid, socket.id);
                                setLanguage(e.target.value);
                            }}
                        >
                            <option value={"python"}>Python</option>
                            <option value={"javascript"}>Javascript</option>
                            <option value={"cpp"}>C++</option>
                            <option value={"java"}>Java</option>
                        </select>
                    </div>

                    <Button
                        disabled={runningCode || submittingCode}
                        color="dark"
                        className="drop-shadow-lg"
                        onClick={e => {
                            e.preventDefault();
                            setRunningCode(true);
                            
                            const runMessage = `${user.name} is running code!`;
                            toast(runMessage);

                            socket.emit("backendCodeExecution", runMessage, uid, socket.uid);

                            // Will be replaced with an async await (on response from execution)
                            setInterval(() => {
                                setRunningCode(false);
                                setSubmittingCode(false);
                            }, 3000);
                        }}
                    >
                        Run
                    </Button>
                    <Button
                        disabled={runningCode || submittingCode}
                        color="dark"
                        className="drop-shadow-lg"
                        onClick={e => {
                            e.preventDefault();
                            setSubmittingCode(true);

                            const submitMessage = `${user.name} is submitting code!`;
                            toast(submitMessage);

                            socket.emit("backendCodeExecution", submitMessage, uid, socket.uid);

                            // Will be replaced with an async await (on response from execution)
                            setInterval(() => {
                                setRunningCode(false);
                                setSubmittingCode(false);
                            }, 3000);
                        }}
                    >
                        Submit
                    </Button>
                </div>
                <div className="flex items-center gap-[21px]">
                    <CountdownTimer />
                    
                    <button onClick={() => setIsSettingsOpen(!isSettingsOpen)} className="w-[71px] h-[46px] bg-darkAccent font-bold py-2 rounded-[15px] border-white border-[3px]">
                        <FaCog className="text-white text-2xl ml-[21px]" />
                    </button>
                    {isSettingsOpen && (
                        <div className="absolute z-50 translate-x-[-75px] translate-y-[195px]">
                            <SettingsPop />
                        </div>
                    )}
                </div>
            </div>
        </section>
    );

};
