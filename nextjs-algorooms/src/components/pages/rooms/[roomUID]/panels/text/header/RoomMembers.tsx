// Module imports
import React, { useContext } from 'react';

// Interface imports
import { memberInterface } from './Interfaces';

// Component imports
import RoomMember from './RoomMember';
import { RoomContext } from '@/contexts/RoomContextLayer';
import { useMutation, useOthers, useSelf, useStorage } from '../../../../../../../../liveblocks.config';
import { AppUserContext } from '@/contexts/AppUserContextLayer';
import { toast } from 'react-toastify';
import createUID from '@/utilities/createUID';
import axios from 'axios';
import buildRoute from '@/utilities/buildRoute';

export default ({

}) => {
  // Code



  const {
    socket,
    uid,
    name
  } = useContext(RoomContext);

  const inRound = useStorage(r => r.inRound);
  const host = useStorage(r => r.host);

  const awaitingQuestion = useStorage(r => r.awaitingQuestion);

  const myPresence = useSelf(me => me.presence);
  const others = useOthers();

  const questionUIDs = useStorage(r => r.questions);

  const finishedQuestions = questionUIDs.length === 0;
  // Starts the round


  const triggerRoundStart = useMutation(async ({ storage }) => {
    storage.set("awaitingQuestion", true);
    
    const questions = storage.get("questions");
    
    const nextQuestionUID = questions.get(questions.length - 1);
    questions.delete(questions.length - 1);
  
    const response = await axios(buildRoute(`/api/questions/verify/${nextQuestionUID}`)).then(r => r).then(r => r.data);
    
    storage.set("awaitingQuestion", false);
    storage.set("currentQuestion", response.question);
    storage.set("inRound", true);

    return response;
  }, [  ]);

  const username = myPresence.username;

  const members = [
    myPresence,
    ...others.map((other) => other.presence)
  ];

  return (
    <section className="flex flex-col bg-darkAccent p-5">
      <span className="text-white uppercase text-xl">{ name }</span>
      <span className="py-6 font-bold text-white">ROOM MEMBERS</span>
      <div className="flex flex-wrap gap-2">
        {
          members.map(member =>
            <RoomMember { ...member } key={createUID(25)} />
          )
        }
      </div>

        { host === username &&
        <button disabled={inRound || awaitingQuestion} className={`${inRound ? "opacity-50" : ""} px-8 py-2 rounded-xl my-4 font-bold bg-greenAccent`}
        onClick={() => {

          // add condition for if no changes have been made to the settings like topics and difficulty
          if (!finishedQuestions) {
            triggerRoundStart();
          } else {
            toast("All questions are completed! Change settings.");

          };

        }}
        >
          START ROUND
        </button>
        }

    </section>
  );
};
