import React from "react";
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import { Button } from "flowbite-react";

const VotingPopUp = (occupied) => {
    const majorNum = Math.ceil(occupied / 2); 

    const renderTime = ({ remainingTime }) => {
        return (
            <div className="">
                <div>{remainingTime}</div>
                <div>seconds</div>
            </div>
        )
    }

    return (
        <div className="text-white h-auto flex flex-col rounded-2xl  shadow-xl border-black border-[3px] items-center bg-[#222C4A]">
            <span className="">Do you want to submit?</span>
            <CountdownCircleTimer
                isPlaying
                duration={1000}
                colors={["#004777", "#F7B801", "#A30000", "#A30000"]}
                colorsTime={[8, 6, 3, 0]}
            >
                {renderTime}
            </CountdownCircleTimer>
            <div className="flex flex-row justify-around">
                <div>
                    <Button color="dark" 
                    className="drop-shadow-lg"
                    onClick={(e) => {
                        e.preventDefault();


                    }}>
                        Agree
                    </Button>
                </div>
                <div>
                    <Button color="dark" 
                    className="drop-shadow-lg">
                        Reject
                    </Button>
                </div>
            </div>

        </div>
    )
}

export default VotingPopUp;