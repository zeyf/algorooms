// Module imports
import React, { useState, useEffect, useRef } from 'react';
import { BsFillSendFill } from 'react-icons/bs';
import { useUser } from '@auth0/nextjs-auth0/client';

// Interface imports
import { textEntryInterface } from './Interfaces';
import { RoomContext } from '@/contexts/RoomContextLayer';
import { TextChatMessage, useMutation, useOthers, useSelf, useUpdateMyPresence } from '../../../../../../../liveblocks.config';
import { LiveList } from '@liveblocks/client';

export default ({

}: textEntryInterface) => {

  const inputRef = useRef(null);

  const myPresence = useSelf(me => me.presence);

  const updatePresence = useUpdateMyPresence();

  const handleTextChatMessageAdd = useMutation(({
    storage,
    setMyPresence
  }, event, MYPRESENCE) => {

    event.preventDefault();
    
    const newMessage:TextChatMessage = {
      username: MYPRESENCE.username,
      color: MYPRESENCE.color,
      message: inputRef.current.value,
      timestamp: Date.now()
    };
    
    storage.get("messages").push(newMessage);

    setMyPresence({
      ...MYPRESENCE,
      isTypingMessage: false
    });

    inputRef.current.value = "";

  }, [  ]);

  const handleGainFocus = () => {
    updatePresence({
      ...myPresence,
      isTypingMessage: true
    });

  };

  const handleLoseFocus = () => {
    updatePresence({
      ...myPresence,
      isTypingMessage: false
    });

  };
  
  const others = useOthers();

  if (!myPresence) {
    return <p>Loading...</p>
  };

  const othersTyping = others.filter(other => other.presence.isTypingCode);
  // ...(myPresence.isTypingMessage ? [ myPresence ] : [  ])

  return (
    <section className="py-5 border-t-[1px] border-black mx-4">
      {/* Body */}
      <form
        onSubmit={e => e.preventDefault()}
        className="flex relative select-text"
      >
        <div className="bg-darkAccent relative w-full rounded overflow-hidden">
          <p className="text-white">
            {
              `${othersTyping.length} users typing...`
            }
          </p>
          <input
            type="message"
            
            ref={inputRef}
            placeholder="Type something simple"
            className="caret-greenAccent bg-transparent text-white p-3 outline-0 w-11/12"

            onBlur={handleLoseFocus}
            onFocus={handleGainFocus}

          />
          <button type="submit"
            onClick={(e) => {
              handleTextChatMessageAdd(e, myPresence);
            }}
          >
            <BsFillSendFill className="absolute right-4 top-4 rotate-45" color="gray" />
          </button>
        </div>
      </form>
    </section>
  );
};
