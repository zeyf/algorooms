// Module imports
import React, { useContext } from 'react';
import { useState, useEffect, useRef } from 'react';
// Add this when text chat is working
// import RoomMember from './header/RoomMember';

// Interface imports
import { textFeedInterface } from './Interfaces';
import { RoomContext } from '@/contexts/RoomContextLayer';
import { useStorage } from '../../../../../../../liveblocks.config';
import formatTime from '@/utilities/formatTime';

export default ({

}: textFeedInterface) => {

  const messages = useStorage(root => root.messages) || [  ];

  const containerRef = useRef(null);

  // This is to make sure the scroll bar scroll down when new messages got added
  useEffect(() => {
    const container = containerRef.current;

    const isBottom = container.scrollHeight - container.scrollTop - 40 === container.clientHeight;

    if(isBottom) {
      container.scrollTo(0, container.scrollHeight);
    }
  }, [ messages.length ]);

  return (
    <section>
      <div className="overflow-y-auto max-h-[400px] bg-darkAccent flex flex-col" ref={containerRef}>
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
                  <div className="flex-shrink-0 text-gray-400 w-full">
                    { `${username}: ${message}\t${formatTime(hour)}:${formatTime(minutes)}` }
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
