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

  const myPresence = useSelf(me => me.presence);
  const others = useOthers();
  
  // Starts the round
  const handleStartRound = useMutation(({ storage }, e) => storage.set("inRound", true), [  ]);

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
        <button disabled={inRound} className={`${inRound ? "opacity-50" : ""} px-8 py-2 rounded-xl my-4 font-bold bg-greenAccent`}
        onClick={handleStartRound}
        >
          START ROUND
        </button>
        }

    </section>
  );
};
