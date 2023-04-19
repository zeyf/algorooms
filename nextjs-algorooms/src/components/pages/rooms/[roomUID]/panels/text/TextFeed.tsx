// Module imports
import React from 'react';
import { useState, useEffect } from 'react';
import { useUser } from '@auth0/nextjs-auth0/client';
import Image from 'next/image';
import io from 'socket.io-client';
// Add this when text chat is working
// import RoomMember from './header/RoomMember';

// Interface imports
import { textFeedInterface } from './Interfaces';

export default ({}: textFeedInterface) => {
  // Code
  const { isLoading, user, error } = useUser();

  //The current feed / messages, test it by putting some string in it
  const [messages, setMessages] = useState<string[]>([
    'Lorem Ipsen or something like that',
  ]);

  useEffect(() => {
    const socket = io();
    socket.on('message', (message: string) => {
      setMessages((messages) => [...messages, message]);
    });
  });

  return (
    <section>
      {/* Body */}
      <div className="overflow-y-auto max-h-[400px] bg-darkAccent flex">
        {/* NOT TESTED */}
        {messages.map((message, index) => (
          <div key={index} className="my-2 mx-2">
            <span className="text-white flex flex-row">
              <div className="flex-shrink-0">
                <Image
                  src={isLoading || !user ? '' : user.picture || ''}
                  alt="user"
                  width={25}
                  height={25}
                  className="rounded-full"
                />
              </div>
              : {message}
            </span>
          </div>
        ))}
      </div>
    </section>
  );
};
