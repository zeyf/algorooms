// Module imports
import React from 'react';
import { useUser } from '@auth0/nextjs-auth0/client';
import Image from 'next/image';
// Add this when text chat is working
// import RoomMember from './header/RoomMember';

// Interface imports
import { textFeedInterface } from './Interfaces';

export default ({}: textFeedInterface) => {
  // Code
  const { isLoading, user, error } = useUser();

  return (
    <section>
      {/* Body */}
      <div className="overflow-y-auto max-h-[400px] bg-darkAccent flex">
        <div className="my-2 mx-2">
          <span className="text-white flex flex-row">
            <Image
              src={isLoading || !user ? '' : user.picture || ''}
              alt="user"
              width={25}
              height={25}
              className="rounded-full"
            />
            : Hello there!
          </span>
        </div>
      </div>
    </section>
  );
};
