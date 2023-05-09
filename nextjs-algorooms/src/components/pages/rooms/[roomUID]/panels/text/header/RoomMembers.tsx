// Module imports
import React, { useContext } from 'react';

// Interface imports
import { memberInterface } from './Interfaces';

// Component imports
import RoomMember from './RoomMember';
import { RoomContext } from '@/contexts/RoomContextLayer';
import { useOthers, useStorage } from '../../../../../../../../liveblocks.config';
import { AppUserContext } from '@/contexts/AppUserContextLayer';

export default ({

}) => {
  // Code

  const {
    socket,
    uid,
    name
  } = useContext(RoomContext);

  const {
    username
  } = useContext(AppUserContext);

  const members = [
    username,
    ...useOthers().map((other) => other.presence.username)
  ];

  return (
    <section className="flex flex-col bg-darkAccent p-5">
      <span className="text-white uppercase text-xl">{ name }</span>
      <span>ROOM MEMBERS</span>
      <div className="flex flex-wrap gap-2">
        {
          members.map((member, colorIndex) =>
            <RoomMember username={member || "?"} colorIndex={colorIndex} />
          )
        }
      </div>
    </section>
  );
};
