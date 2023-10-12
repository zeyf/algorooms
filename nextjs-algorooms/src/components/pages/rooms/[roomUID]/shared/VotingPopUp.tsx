import React, { useState } from "react";
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import { Button } from "flowbite-react";
import { useMutation, useStorage } from "../../../../../../liveblocks.config";

const VotingPopUp = (occupied) => {
    const majorNum = Math.ceil(occupied / 2); 

    
    // Keep track of whether or not 
    const [hasAccepted, setHasAccepted] = useState(false);
    const [hasRejected, setHasRejected] = useState(false);

    const acceptVoteCount = useStorage(r => r.acceptVoteCount);
    const rejectVoteCount = useStorage(r => r.rejectVoteCount);

    const setAcceptVoteCount = useMutation(({storage}, newAcceptVoteCount) => {
      storage.set("acceptVoteCount", newAcceptVoteCount)
    }, []);

    const setRejectVoteCount = useMutation(({storage}, newRejectVoteCount) => {
      storage.set("rejectVoteCount", newRejectVoteCount)
    }, []);

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
                    <Button
                      color="dark" 
                      className="drop-shadow-lg"
                      disabled={hasAccepted}
                      onClick={(e) => {
                          e.preventDefault();

                          if (hasAccepted) {
                            return;
                          }

                          if (hasRejected) {
                            setHasRejected(false);
                            setRejectVoteCount(rejectVoteCount - 1);
                          }

                          setHasAccepted(true);
                          setAcceptVoteCount(acceptVoteCount + 1);
                      }}
                    >
                        Agree
                    </Button>
                </div>
                <div>
                    <Button
                      color="dark" 
                      className="drop-shadow-lg"
                      disabled={hasRejected}
                      onClick={(e) => {
                        e.preventDefault();

                        if (hasRejected) {
                          return;
                        }

                        if (hasAccepted) {
                          setHasAccepted(false);
                          setAcceptVoteCount(acceptVoteCount - 1);
                        }

                        setHasRejected(true);
                        setRejectVoteCount(rejectVoteCount + 1);
                    }}
                    >
                      Reject
                    </Button>
                </div>
            </div>

        </div>
    )
}

export default VotingPopUp;