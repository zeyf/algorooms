// Module imports
import React, { useContext } from "react";
import { useState, useRef, useEffect } from 'react'

// Interface imports
import { countdownTimerInterface } from "./Interfaces";
import { useMutation, useStorage } from "../../../../../../../../liveblocks.config";
import { RoomContext } from "@/contexts/RoomContextLayer";
import { toast } from "react-toastify";

export default ({

}:countdownTimerInterface) => {

    const minutesLeft = useStorage(r => r.minutesLeft);
    const secondsLeft = useStorage(r => r.secondsLeft);
    const startMinutes = useStorage(r => r.startMinutes);
    const startSeconds = useStorage(r => r.startSeconds);
    const inRound = useStorage(r => r.inRound);

    const {
        socket,
        uid
    } = useContext(RoomContext);


    const changeTime = useMutation(({ storage }, min, sec) => {

        if (sec > 0)
            storage.set("secondsLeft", sec - 1);
        else {
            if (min > 0) {
                storage.set("minutesLeft", min - 1);
                storage.set("secondsLeft", 59);
            };
        };

    }, [  ]);

    const handleEndRound = useMutation(({ storage }, startMinutes,startSeconds) => {
      storage.set("minutesLeft", startMinutes);
      storage.set("secondsLeft", startSeconds);
      storage.set("inRound", false);
  }, [  ]);

    useEffect(() => {   


        if (inRound && minutesLeft !== null && secondsLeft !== null) {

            const timerID = setInterval(() => {
                if (minutesLeft === 0 && secondsLeft === 0) {
                    handleEndRound(startMinutes, startSeconds);
                    clearInterval(timerID);

                    toast("The round is over!");
                } else
                    changeTime(minutesLeft, secondsLeft);
            }, 1000);
            
            return () => clearInterval(timerID);
        };

    }, [ inRound, minutesLeft, secondsLeft ]);

    if (minutesLeft === null || secondsLeft === null || startMinutes === null)
        return <p>Loading...</p>

    return (
        <div className="text-white bg-[#051135] flex justify-center items-center rounded-xl drop-shadow-lg">
            <h3 className="font-bold text-lg">
                {`${minutesLeft.toString()} : ${secondsLeft.toString().padStart(2, '0')}`}
            </h3>
        </div>
    );

};
