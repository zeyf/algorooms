// Module imports
import React from 'react';
import { useEffect, useRef } from 'react';

// Interface imports
import { textFeedInterface } from './Interfaces';
import { useStorage } from '../../../../../../../liveblocks.config';
import formatTime from '@/utilities/formatTime';

export default ({

}: textFeedInterface) => {

  // Read in all messages
  const messages = useStorage(root => root.messages);

  // Create reference for the messages div
  const containerRef = useRef(null);

  // This is to make sure the scroll bar scroll down when new messages got added
  useEffect(() => {

    // Get the reference to the div
    const container = containerRef.current;

    // Are we at the very bottom of the div
    const isBottom = container.scrollHeight - container.scrollTop - 40 === container.clientHeight;

    // Are we at the very top of the div
    const isTop = container.scrollTop === 0;

    // If we are at the bottom or at the top, scroll to the very bottom
    if (isBottom || isTop)
      container.scrollTo(0, container.scrollHeight);

  // The messages length is a dependency for the useEffect as we want to scroll down on addition of every new message
  }, [ messages.length ]);

  return (
      <section className="flex-[3] overflow-y-auto bg-lightAccent flex flex-col h-full" ref={containerRef}>
        {/* NOT TESTED */}
        {

          // Display all messages

          messages.map(({
            message,
            username,
            timestamp,
            color
          }, index) => {
            
            // Get the hour and time from the timestamp
            const date = new Date(timestamp);
            const hour = date.getHours(),
                  minutes = date.getMinutes();

            return (
              <div key={index} className="my-2 mx-2">
                <span className="text-white">
                  <div className="flex-shrink-0 text-gray-400 w-full">
                    <span style={{ color: color}}>
                      {`${username}`}
                    </span>
                    { `: ${message}\t${formatTime(hour)}:${formatTime(minutes)}` }
                  </div>
                </span>
              </div>
            )
          })
        }
      </section>
  );
};
