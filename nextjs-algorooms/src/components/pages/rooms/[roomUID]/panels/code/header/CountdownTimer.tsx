// Module imports
import React from "react";
import { useState, useRef, useEffect } from 'react'

// Interface imports
import { countdownTimerInterface } from "./Interfaces";

export default ({

}:countdownTimerInterface) => {

    // Code
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

    // resets the timer
    const reset = () => setTime([minutes, seconds]);

    useEffect(() => {
        const timerID = setInterval(() => tick(), 1000);
        return () => clearInterval(timerID);
    })

    return (
        <div className="text-white bg-[#051135] w-[95px] h-[46px] flex justify-center items-center rounded-xl drop-shadow-lg">
            <h3 className="font-bold text-lg">
                {`${mins.toString()} : ${secs.toString().padStart(2, '0')}`}
            </h3>
        </div>
    );

};
