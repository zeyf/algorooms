// Module imports
import React from 'react';

// Interface imports
import { feedMessageInterface } from './Interfaces';
import RoomMember from './header/RoomMember';

const FeedMessage = ({ member, message, date }: feedMessageInterface) => {
  return (
    <div className="flex flex-row ">
      <RoomMember member="test" backgroundColor="bg-greenAccent" />
      {message}
    </div>
  );
};

export default FeedMessage;
