// Module imports
import React from 'react';

// Interface imports
import { roomMemberInterface } from './Interfaces';
import Link from 'next/link';

const colors = [
  "#650cec",
  "#3960f7",
  "#424d71",
  "#d91072",
  "#af90fd",
  "#60aa59"
];

export default ({
  username,
  colorIndex
}: roomMemberInterface) => {
  
  return (
    <Link
      href={`/profile/${username}`}
      className="flex flex-col">
      <div
        className={`${colors[colorIndex]} h-10 w-10 rounded-full flex justify-center items-center`}
      >
        <div>{username[0].toUpperCase()}</div>
      </div>
      <div className="text-white text-center">{ username }</div>
    </Link>
  );
};
