// Module imports
import React, { useContext } from 'react';

// Interface imports
import { memberInterface } from './Interfaces';

// Component imports
import RoomMember from './RoomMember';
import { RoomContext } from '@/contexts/RoomContextLayer';
import { useOthers, useSelf, useStorage } from '../../../../../../../../liveblocks.config';
import { AppUserContext } from '@/contexts/AppUserContextLayer';

export default ({

}) => {
  // Code

  const {
    socket,
    uid,
    name
  } = useContext(RoomContext);

  const myPresence = useSelf(me => me.presence);
  const others = useOthers();

  if (!myPresence)
    return <p>Loading...</p>

  const members = [
    myPresence,
    ...others.map((other) => other.presence)
  ];

  return (
    <section className="flex flex-col bg-darkAccent p-5">
      <span className="text-white uppercase text-xl">{ name }</span>
      <span>ROOM MEMBERS</span>
      <div className="flex flex-wrap gap-2">
        {
          members.map(member =>
            <RoomMember { ...member } />
          )
        }
      </div>
    </section>
  );
};
