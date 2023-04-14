// Module imports
import React, { useState } from "react";
import { Select, Option } from "@material-tailwind/react";
import { Button } from "flowbite-react";
import SettingsPop from "../../../shared/settingsPop";
import { FaCog } from "react-icons/fa";

// Interface imports
import { headerInterface } from "./Interfaces";
import CountdownTimer from "./CountdownTimer";

export default ({

}:headerInterface) => {

    // Code
    const [isSettingsOpen, setIsSettingsOpen] = useState(false);

    return (
        <section>
            <div className="w-[822px] flex flex-row space-x-5 items-center p-1 justify-between">
                <div className="flex items-center gap-[21px]">
                    <div className="w-[200px]">
                        <Select label="Select Language" className="drop-shadow-lg" color="blue">
                            <Option>Python</Option>
                            <Option>Javascript</Option>
                        </Select>
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
