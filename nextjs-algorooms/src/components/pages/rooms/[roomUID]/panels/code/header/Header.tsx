// Module imports
import React, { useContext, useEffect, useState } from "react";
import { Select, Option } from "@material-tailwind/react";
import { Button } from "flowbite-react";
import SettingsPop from "../../../shared/SettingsPopUp";
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

    const {
        socket,
        uid,

        language,
        setLanguage,
        runningCode,
        setRunningCode,
        submittingCode,
        setSubmittingCode,
        setTopics,
        setDifficulty,
        setLobbyAccess,
    } = useContext(RoomContext);

    const {
        user
    } = useUser();

    const buildSettingsChangeToastMessage = (newTopics, newDifficulty, newLobbyAccess) => {
        let toastMessage = [  ];

        if (newDifficulty !== null)
            toastMessage.push(`Difficulty changed to: ${newDifficulty}`);
        
        if (newTopics !== null)
            toastMessage.push(`Topics changed to: ${newTopics.toString().replace(",", ", ")}`);

        if (newLobbyAccess !== null)
            toastMessage.push(`Lobby Access changed to: ${newLobbyAccess}`);

        return toast(toastMessage.join(", "));
    };

    useEffect(() => {
        socket.on("frontendLanguageChange", (language, socketUser) => {
            toast(`Language changed to: ${language}`);
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

        socket.on("frontendSettingsChange", (settingsPayload, username, socketUser) => {

            setTopics(settingsPayload.topics);
            setDifficulty(settingsPayload.difficulty);
            setLobbyAccess(settingsPayload.lobbyAccess);

            toast(buildSettingsChangeToastMessage(
                settingsPayload.topics,
                settingsPayload.difficulty,
                settingsPayload.lobbyAccess
            ));

        });

    }, [  ]);

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
                                toast(`Language changed to: ${e.target.value}`);
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
                            <SettingsPop
                                {...{
                                    isSettingsOpen,
                                    setIsSettingsOpen,
                                    buildSettingsChangeToastMessage
                                }   }
                            />
                        </div>
                    )}
                </div>
            </div>
        </section>
    );

};
