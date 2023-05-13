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
      className="text-white text-center px-2 py-1 flex flex-col rounded-lg"
    
      // Link to the username
      href={`/profile/${username}`}

      // Set-force the background color
      style={{
        backgroundColor: color
      }}
    >
      { username }
    </Link>
  );





};
