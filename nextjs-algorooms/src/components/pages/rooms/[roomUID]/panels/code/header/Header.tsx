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

export default ({

}:headerInterface) => {

    // Code
    const [
        isSettingsOpen,
        setIsSettingsOpen
    ] = useState(false);

    const [
        selectedLanguage,
        setSelectedLanguage
    ] = useState("Default");

    const {
        socket,
        uid
    } = useContext(RoomContext);

    useEffect(() => {
        socket.on("frontendLanguageChange", (language, socketUser) => {
            setSelectedLanguage(language);
        });
    }, [  ])

    return (
        <section>
            <div className="w-[822px] flex flex-row space-x-5 items-center p-1 justify-between">
                <div className="flex items-center gap-[21px]">
                    <div className="w-[200px]">
                        <select
                            // If you are the host, true. Otherwise, false.
                            disabled={!true}
                            placeholder="Select Language"
                            className="drop-shadow-lg"
                            color="blue"
                            value={selectedLanguage}
                            onChange={e => {
                                socket.emit("backendLanguageChange", e.target.value, uid, socket.id);
                                setSelectedLanguage(e.target.value);
                            }}
                        >
                            <option>Python</option>
                            <option>Javascript</option>
                        </select>
                    </div>

                    <Button href="/" color="dark" className="drop-shadow-lg">Run</Button>
                    <Button href="/" color="dark" className="drop-shadow-lg">Submit</Button>
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
