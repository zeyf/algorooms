// Module imports
import React, { useContext } from 'react';
import { useState, useEffect } from 'react';
// Add this when text chat is working
// import RoomMember from './header/RoomMember';

// Interface imports
import { textFeedInterface } from './Interfaces';
import { RoomContext } from '@/contexts/RoomContextLayer';

export default ({

}: textFeedInterface) => {
  // Code

  const {
    messages,
    socket
  } = useContext(RoomContext);

  return (
    <section>
      <div className="overflow-y-auto max-h-[400px] bg-darkAccent flex flex-col">
        {/* NOT TESTED */}
        {
          messages.map(({
            message,
            username,
            timestamp
          }, index) => {
            
            const date = new Date(timestamp);
            const hour = date.getHours(),
                  minutes = date.getMinutes();

            return (
              <div key={index} className="my-2 mx-2">
                <span className="text-white flex flex-row">
                  <div className="flex-shrink-0 text-gray-400">
                    { `${username}: ${message}\t${hour}:${minutes}` }
                  </div>
                </span>
              </div>
            )
          })
        }
      </div>
    </section>
  );
};
