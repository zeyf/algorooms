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
    
    // Keep track of whether or not user has voted for accept or reject
    // Need both in the case user has not selected either  option
    // const [hasAccepted, setHasAccepted] = useState(false);
    // const [hasRejected, setHasRejected] = useState(false);

    const acceptVoteCount = useStorage(r => r.acceptVoteCount);
    const rejectVoteCount = useStorage(r => r.rejectVoteCount);
    const isVotingOpen = useStorage(r => r.isVotingOpen);
    const startMinutes = useStorage(r => r.startMinutes);
    const startSeconds = useStorage(r => r.startSeconds);

    const myPresence = useSelf(me => me.presence);
    const others = useOthers();
    const othersUsernames = others.map(other => other.presence.username);

  const updatePresence = useUpdateMyPresence();

    // Update self presence to reflect typing onChange or onFocus of the input element
    const handleAcceptVote = () => {
      updatePresence({
      ...myPresence,
      hasAccepted: true,
      hasRejected: false
    })
    setAcceptVoteCount(acceptVoteCount + 1);
    setRejectVoteCount(rejectVoteCount - 1);
  };

    const handleRejectVote = () => {
      updatePresence({
      ...myPresence,
      hasAccepted: false,
      hasRejected: true
    })
    setAcceptVoteCount(acceptVoteCount - 1);
    setRejectVoteCount(rejectVoteCount + 1);
  };

    const resetMyVote = () => {
      updatePresence({
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
      setIsVotingOpen(!isVotingOpen);
      resetMyVote();
      setRejectVoteCount(0);
      setAcceptVoteCount(0);
    }

    useEffect(() => {
      (async () => {

        // If there has not been enough votes for either action, wait until there are
        if ((acceptVoteCount < majorNum) && (rejectVoteCount < majorNum)) {
          return;
        }

        if (rejectVoteCount >= majorNum) {
          // If there are enough votes to reject, notify the room
          toast("Voting cancelled");
        } else {
          // Else, run the code
          toast("Submitting the code...")
          await handleCodeExecution("SUBMIT", startMinutes, startSeconds);
        }

        // Close the voting modal and reset the vote counts to 0
        resetVoting();

        
        
      })();

    }, [acceptVoteCount, rejectVoteCount]);

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
                duration={15}
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
                      disabled={myPresence.hasAccepted}
                      onClick={(e) => {
                          e.preventDefault();

                          // If the user wants to vote to accept again, don't allow them
                          if (myPresence.hasAccepted) {
                            return;
                          }

                          // If the user already voted to reject, but wants to change their vote,
                          // take away their reject vote
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