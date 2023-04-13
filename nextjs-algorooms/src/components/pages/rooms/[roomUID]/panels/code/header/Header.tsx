// Module imports
import React from "react";
import { Select, Option } from "@material-tailwind/react";
import { Button } from "flowbite-react";


// Interface imports
import { headerInterface } from "./Interfaces";
import CountdownTimer from "./CountdownTimer";

export default ({

}:headerInterface) => {

    // Code


    return (
        <section>
            <div className="w-[822px] flex flex-row space-x-5 items-center p-1">
                <div className="w-[200px]">
                    <Select label="Select Language" className="drop-shadow-lg" color="blue">
                        <Option>Python</Option>
                        <Option>Javascript</Option>
                    </Select>
                </div>

                <Button href="/" color="dark" className="drop-shadow-lg">Run</Button>
                <CountdownTimer />
            </div>
        </section>
    );

};
