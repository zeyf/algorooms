// Module imports
import React, { useContext, useEffect, useState, useRef } from "react";
import { Button } from "flowbite-react";
import SettingsPop from "../../../shared/SettingsPopUp";
import { FaCog } from "react-icons/fa";
import WhiteBoard from "../WhiteBoard";

// Interface imports
import { headerInterface } from "./Interfaces";
import CountdownTimer from "./CountdownTimer";
import { RoomContext } from "@/contexts/RoomContextLayer";
import { toast } from "react-toastify";
import { AppUserContext } from "@/contexts/AppUserContextLayer";
import { useMutation, useStorage, useOthers } from "../../../../../../../../liveblocks.config";
import languageMapper from "@/utilities/languageMapper";
import buildRoute from "@/utilities/buildRoute";
import axios from "axios";

export default ({

}:headerInterface) => {

    const CLIENT_ID = process.env.EXEC_CLIENT_ID, CLIENT_SECRET = process.env.EXEC_CLIENT_SECRET;

    // Code
    const [
        isSettingsOpen,
        setIsSettingsOpen
    ] = useState(false);

    const {
        socket,
        uid,
        runningCode,
        setRunningCode,
        submittingCode,
        setSubmittingCode,
        setTopics,
        setDifficulty,
        setLobbyAccess,
        setWhiteBoard,
        whiteBoard
    } = useContext(RoomContext);

    const {
        username
    } = useContext(AppUserContext);

    const inRound = useStorage(r => r.inRound);
    const awaitingQuestion = useStorage(r => r.awaitingQuestion);
    const startMinutes = useStorage(r => r.startMinutes);
    const others = useOthers();
    // Get others people usernames
    const othersUsernames = others.map(other => other.presence.username);

    const buildSettingsChangeToastMessage = (usernameOfChanger, newTopics, newDifficulty, newLobbyAccess) => {
        let toastMessage = [  ];

        if (newDifficulty !== null)
            toastMessage.push(`Difficulty changed to: ${newDifficulty}`);
        
        if (newTopics !== null)
            toastMessage.push(`Topics changed to: ${newTopics.toString().replace(/,/gi, ", ")}`);

        if (newLobbyAccess !== null)
            toastMessage.push(`Lobby Access changed to: ${newLobbyAccess}`);

        return toastMessage.length > 0 ? `${usernameOfChanger} had -- ` + toastMessage.join(", ") : null;
    };

    // Change the timer when round end or question get submitted
    const handleEndRound = useMutation(({ storage }, startMin) => {
        storage.set("inRound", false);
        storage.set("minutesLeft", startMin);
        storage.set("secondsLeft", 0);
    }, [  ]);

    useEffect(() => {
        socket.on("frontendLanguageChange", (usernameOfChanger, language, socketUser) => {
            toast(`${usernameOfChanger} changed language to: ${language}`);
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

        socket.on("frontendSettingsChange", (settingsPayload, senderUsername, socketUser) => {

            setIsSettingsOpen(false);

            setTopics(settingsPayload.topics);
            setDifficulty(settingsPayload.difficulty);
            setLobbyAccess(settingsPayload.lobbyAccess);

            const toastMessage = buildSettingsChangeToastMessage(
                senderUsername,
                settingsPayload.topics,
                settingsPayload.difficulty,
                settingsPayload.lobbyAccess
            );
            if (toastMessage !== null){
                toast(toastMessage);

            }

        });

    }, [  ]);

    // Handle closing the settings popup when user clicks away
    const settingsButtonRef = useRef(null);

    useEffect(() => {
        const handleOutsideClick = (event) => {
          if (isSettingsOpen && !settingsButtonRef.current.contains(event.target)) {
            setIsSettingsOpen(false);
          }
        };
      
        document.addEventListener("click", handleOutsideClick);
      
        return () => {
          document.removeEventListener("click", handleOutsideClick);
        };
    }, [isSettingsOpen]);  

    // Get the current editor language
    const editorLanguage = useStorage(({ language }) => language);

    // Handle the change of the current editor language
    const handleLanguageChange = useMutation(({ storage }, event) => storage.set("language", event.target.value.toLowerCase()), [  ]);

    const handleCodeExecution = useMutation(async ({
        storage,
        self
    }, executionType, langMapper = languageMapper, clientId = CLIENT_ID, clientSecret = CLIENT_SECRET) => {

        const editorLang:any = storage.get("language");

        const submission = executionType === "SUBMIT";
        const run = executionType === "RUN";

        if (submission)
            storage.set("submitCodeInQueue", true);
        else if (run)
            storage.set("runCodeInQueue", true);

        const editorText = storage.get("activeEditorTexts").get(editorLang);

        const currentQuestionData = storage.get("currentQuestion");

        const payload = {
            usernames: [self.presence.username, ...othersUsernames],
            type: submission ? "SUBMIT" : ( run ? "RUN" : "ERROR" ),
            clientId,
            clientSecret,
            script: editorText,
            relativeLanguage: editorLang,
            timestamp: Date.now(),
            questionTitle: currentQuestionData.title,
            questionUID: currentQuestionData.uid,
            ...langMapper[editorLang].jDoodleAPITemplateConfiguration
        };

        payload.executionLanguage = payload.language;
        
        const response = await axios.post(buildRoute("/api/rooms/execute"), payload).then(r => r).then(r => r.data);

        const {
            state
        } = response.result;

        storage.set("ranCodeOutputOnQuestion", response.result);

        if (state === "ACCEPTED") {
            toast(`Congratulations on solving ${storage.get("currentQuestion").title}!`);
            handleEndRound(startMinutes);
        }
        
        storage.set("submitCodeInQueue", false);
        storage.set("runCodeInQueue", false);
    }, [  ]);


    const handleCodeReset = useMutation(({ storage }) => {

        const currentLanguageInView:any = storage.get("language");
        storage.get("activeEditorTexts").set(currentLanguageInView, storage.get("resetEditorTexts").get(currentLanguageInView));

    }, [  ]);

    return (
        <section>
            <div className="w-full flex flex-row space-x-5 items-center justify-between py-5">
                <div className="flex items-center gap-[21px]">
                    <div className="w-[200px]">
                        <select

                            // If you are the host, true. Otherwise, false.
                            disabled={runningCode || submittingCode}
                            
                            // This will hold the value of the current langauge
                            value={editorLanguage}

                            placeholder="Select Language"
                            className="drop-shadow-lg w-full"
                            color="blue"

                            // Change the language and communicate the changes
                            onChange={e => {
                                handleLanguageChange(e);
                                socket.emit("backendLanguageChange", e.target.value, username, uid, socket.id);
                                toast(`${username} changed language to: ${e.target.value}`);
                            }}
                        >
                            <option value={"python"}>Python</option>
                            <option value={"javascript"}>Javascript</option>
                            {/*
                            <option value={"cpp"}>C++</option>
                            <option value={"java"}>Java</option>
                            */}
                        </select>
                    </div>

                    <Button
                        disabled={runningCode || submittingCode}
                        color="dark"
                        className="drop-shadow-lg"
                        onClick={e => {
                            e.preventDefault();
                            handleCodeReset();
                        }}
                    >
                        Reset Code
                    </Button>

                    <Button
                        disabled={runningCode || submittingCode}
                        color="dark"
                        className="drop-shadow-lg"
                        onClick={e => {

                            e.preventDefault();
                            handleCodeExecution("RUN");

                            setRunningCode(true);
                            
                            const runMessage = `${username} is running code!`;
                            toast(runMessage);

                            // socket.emit("backendCodeExecution", runMessage, uid, socket.uid);

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
                            handleCodeExecution("SUBMIT");

                            setSubmittingCode(true);

                            const submitMessage = `${username} is submitting code!`;
                            toast(submitMessage);

                            // socket.emit("backendCodeExecution", submitMessage, uid, socket.uid);

                            // Will be replaced with an async await (on response from execution)
                            setInterval(() => {
                                setRunningCode(false);
                                setSubmittingCode(false);
                            }, 3000);
                        }}
                    >
                        Submit
                    </Button>
                    <Button
                        color="dark"
                        className="drop-shadow-lg"
                        onClick={() => {
                            setWhiteBoard(!whiteBoard)
                        }}
                    >
                        WhiteBoard
                    </Button>
                </div>
                <div className="flex items-center gap-[21px]">
                    <CountdownTimer />
                    
                    <button 
                        ref={settingsButtonRef}
                        onClick={() => setIsSettingsOpen(!isSettingsOpen)} 
                        className={` ${inRound ? "opacity-50" : ""} w-[71px] h-[46px] bg-darkAccent font-bold py-2 rounded-[15px] border-white border-[3px]` }

                        disabled={inRound || awaitingQuestion}
                    >   
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