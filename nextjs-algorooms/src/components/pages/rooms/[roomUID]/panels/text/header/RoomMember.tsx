// Module imports
import React from 'react';

// Interface imports
import { roomMemberInterface } from './Interfaces';
import Link from 'next/link';

export default ({
  username,
  color
}: roomMemberInterface) => {
  
  return (
    <Link
      href={`/profile/${username}`}
      className="text-white text-center px-2 py-1 flex flex-col rounded-lg"
      style={{
        backgroundColor: color
      }}
    >
      { username }
    </Link>
  );
};
