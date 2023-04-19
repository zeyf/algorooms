// Module imports
import React from 'react';
import { useState, useEffect } from 'react';
import io from 'socket.io-client';
// Add this when text chat is working
// import RoomMember from './header/RoomMember';

// Interface imports
import { textFeedInterface } from './Interfaces';

export default ({}: textFeedInterface) => {
  // Code

  //The current feed / messages, test it by putting some string in it, now have name along with it
  const [messages, setMessages] = useState<string[][]>([[
    'Khoa',
    'Lorem Ipsen or something like that',
  ]
  ]);

  useEffect(() => {
    const socket = io();
    socket.on('message', (message: string, name: string) => {
      setMessages((messages) => [...messages, [name, message]]);
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
              <div className="flex-shrink-0 text-gray-400">
                {message[0]}
              </div>
              : {message[1]}
            </span>
          </div>
        ))}
      </div>
    </section>
  );
};
