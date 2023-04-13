// Module imports
import React from 'react';

// Interface imports
import { memberInterface, roomMembersInterface } from './Interfaces';

// Component imports
import RoomMember from './RoomMember';

export default ({ members }: roomMembersInterface) => {
  // Code

  return (
    <section className="flex flex-col bg-darkAccent p-5">
      <span className="text-white uppercase text-xl">CS Amigos</span>
      <div className="flex flex-wrap gap-2">
        {members.map((member: memberInterface) => (
          <RoomMember member={member.name} backgroundColor={member.color} />
        ))}
      </div>
    </section>
  );
};
