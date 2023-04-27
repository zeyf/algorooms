// Module imports
import React, { useContext } from 'react';

// Interface imports
import { memberInterface } from './Interfaces';

// Component imports
import RoomMember from './RoomMember';
import { RoomContext } from '@/contexts/RoomContextLayer';

export default ({

}) => {
  // Code

  const {
    socket,
    uid,
    name
  } = useContext(RoomContext);

  const {
    members
  } = useContext(RoomContext);

  return (
    <section className="flex flex-col bg-darkAccent p-5">
      <span className="text-white uppercase text-xl">{ name }</span>
      <div className="flex flex-wrap gap-2">
        {members.map(({
          username
        }:any, colorIndex: number) => (
          <RoomMember
            username={username}
            colorIndex={colorIndex}
          />
        ))}
      </div>
    </section>
  );
};
