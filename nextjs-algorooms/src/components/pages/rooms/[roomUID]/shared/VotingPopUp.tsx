import React, { useEffect, useState } from "react";
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import { Button } from "flowbite-react";
import { useMutation, useOthers, useSelf, useStorage, useUpdateMyPresence } from "../../../../../../liveblocks.config";
import languageMapper from "@/utilities/languageMapper";
import { toast } from "react-toastify";
import buildRoute from "@/utilities/buildRoute";
import axios from "axios";

const VotingPopUp = ({ occupied }) => {
    const majorNum = Math.ceil(occupied / 2); 

    const CLIENT_ID = process.env.EXEC_CLIENT_ID, CLIENT_SECRET = process.env.EXEC_CLIENT_SECRET;
    
    const acceptVoteCount = useStorage(r => r.acceptVoteCount);
    const rejectVoteCount = useStorage(r => r.rejectVoteCount);
    const isVotingOpen = useStorage(r => r.isVotingOpen);
    const startMinutes = useStorage(r => r.startMinutes);
    const startSeconds = useStorage(r => r.startSeconds);
    const remainingTime = useStorage(r => r.remainingTime);

    const myPresence = useSelf(me => me.presence);
    const others = useOthers();
    const othersUsernames = others.map(other => other.presence.username);

    const updatePresence = useUpdateMyPresence();

    // Update self presence to reflect typing onChange or onFocus of the input element
    const handleAcceptVote = () => {
      const hasRejected = myPresence.hasRejected ? 1 : 0;
      setAcceptVoteCount(acceptVoteCount + 1);
      setRejectVoteCount(rejectVoteCount - hasRejected);
      updatePresence({
        ...myPresence,
        hasAccepted: true,
        hasRejected: false
      })
    };

    const handleRejectVote = () => {
      const hasAccepted = myPresence.hasAccepted ? 1 : 0;
      setRejectVoteCount(rejectVoteCount + 1);
      setAcceptVoteCount(acceptVoteCount - hasAccepted);
      updatePresence({
        ...myPresence,
        hasAccepted: false,
        hasRejected: true
      });
  };

    const resetMyVote = () => {
      updatePresence({
        ...myPresence,
        hasAccepted: false,
        hasRejected: false
      })
    };


    const setAcceptVoteCount = useMutation(({storage}, newAcceptVoteCount) => {
      storage.set("acceptVoteCount", newAcceptVoteCount)
    }, []);

    const setRejectVoteCount = useMutation(({storage}, newRejectVoteCount) => {
      storage.set("rejectVoteCount", newRejectVoteCount)
    }, []);

    const setIsVotingOpen = useMutation(({ storage }, newIsVotingOpen) => {
      storage.set("isVotingOpen", newIsVotingOpen);
    }, [ ]);

    const handleEndRound = useMutation(({ storage }, startMinutes, startSeconds) => {
      storage.set("minutesLeft", startMinutes);
      storage.set("secondsLeft", startSeconds);
      storage.set("inRound", false);
  }, [  ]);

    const handleCodeExecution = useMutation(async ({
      storage,
      self
  }, executionType, startMinutes, startSeconds, langMapper = languageMapper, clientId = CLIENT_ID, clientSecret = CLIENT_SECRET) => {

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
          handleEndRound(startMinutes, startSeconds);
      }
      
      storage.set("submitCodeInQueue", false);
      storage.set("runCodeInQueue", false);
  }, [  ]);

    const resetVoting = () => {
      console.log("RESETTING");
      setIsVotingOpen(false);
      // This timer acts as a buffer so that the 
      // non-hosts timers doesn't overwrite the time reset
      setTimeout(() => {
        changeRemainingTime(60);
        resetMyVote();
        setRejectVoteCount(0);
        setAcceptVoteCount(0);
      }, 350)
    }

    useEffect(() => {
      console.log("ACCEPT", acceptVoteCount, "REJECT", rejectVoteCount, "MAJOR", majorNum);
      console.log("TRYING TO SUBMIT")
      // If there has not been enough votes for either action, wait until there are
      if ((acceptVoteCount < majorNum) && (rejectVoteCount < majorNum)) {
        return;
      }
      const isReject = rejectVoteCount >= majorNum;
      // Close the voting modal and reset voting info
      resetVoting();

      (async () => {
        console.log("MAJORITY");
        if (isReject) {
          // If there are enough votes to reject, notify the room
          toast("Voting cancelled");
        } else {
          // Else, run the code
          toast("Submitting the code...")
          await handleCodeExecution("SUBMIT", startMinutes, startSeconds);
        }

      })();

    }, [acceptVoteCount, rejectVoteCount]);
    
    const changeRemainingTime = useMutation(({ storage }, remainingTime) => {
        storage.set("remainingTime", remainingTime);
    }, [ ]);


    const renderTime = ({ remainingTime }) => {
        changeRemainingTime(remainingTime)
        return (
            <div className="text-4xl">
                <div>{remainingTime}</div>
            </div>
        )
    }

    return (
        <div className="text-white h-auto flex flex-col rounded-2xl shadow-xl items-center bg-[#222C4A]">
            <span className="font-bold">Do you want to submit?</span>
            <CountdownCircleTimer
                isPlaying
                duration={60}
                initialRemainingTime={remainingTime}
                colors={["#004777", "#F7B801", "#A30000", "#A30000"]}
                colorsTime={[45, 30, 15, 0]}
                onComplete={() => {
                  // Submit the code if the timer runs out
                  resetVoting();
                  (async () => {
                    toast("Submitting the code...")
                    await handleCodeExecution("SUBMIT", startMinutes, startSeconds);
                  })();

                  // Close the voting modal and reset voting info
                }}
            >
                {renderTime}
          </CountdownCircleTimer>
            <div className="flex flex-row justify-around w-full p-2">
                <div>
                    <Button
                      color="dark" 
                      className="drop-shadow-lg"
                      disabled={myPresence.hasAccepted}
                      onClick={(e) => {
                          e.preventDefault();

                          // If the user wants to vote to accept again, don't allow them
                          if (myPresence.hasAccepted) {
                            return;
                          }

                          handleAcceptVote();                       
                      }}
                    >
                        Agree
                    </Button>
                </div>
                <div>
                    <Button
                      color="dark" 
                      className="drop-shadow-lg"
                      disabled={myPresence.hasRejected}
                      onClick={(e) => {
                        e.preventDefault();

                        // If the user wants to vote to reject again, don't allow them
                        if (myPresence.hasRejected) {
                          return;
                        }

                        handleRejectVote();
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