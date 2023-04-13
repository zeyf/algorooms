// Module imports
import React from 'react';

// Interface imports
import { roomMemberInterface } from './Interfaces';

export default ({ member, backgroundColor }: roomMemberInterface) => {
  return (
    <div className="flex flex-col">
      <div
        className={`${backgroundColor} h-10 w-10 rounded-full flex justify-center items-center`}
      >
        <div>{member[0].toUpperCase()}</div>
      </div>
      <div className="text-white">{member}</div>
    </div>
  );
};
