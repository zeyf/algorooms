// Module imports
import React, { useState, useEffect, useRef } from 'react';
import { BsFillSendFill } from 'react-icons/bs';
import { useUser } from '@auth0/nextjs-auth0/client';

// Interface imports
import { textEntryInterface } from './Interfaces';
import { RoomContext } from '@/contexts/RoomContextLayer';
import { TextChatMessage, useMutation, useOthers, useSelf, useUpdateMyPresence } from '../../../../../../../liveblocks.config';
import { LiveList } from '@liveblocks/client';
import TextTypingAnimation from './TextTypingAnimation';

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

  const handleStartedTyping = () => !myPresence.isTypingCode && updatePresence({
    ...myPresence,
    isTypingMessage: true
  });

  const handleStoppedTyping = () => updatePresence({
    ...myPresence,
    isTypingMessage: false
  });
  
  const others = useOthers();

  const othersTyping = others.filter(other => other.presence.isTypingMessage);

  const buildUsersTypingMessage = () => {
    if (othersTyping.length === 0)
      return "";
    else if (othersTyping.length === 1)
      return `${othersTyping[0].presence.username} is typing...`;
    else
      return "Several users are typing...";
  };

  return (
    <section className="h-[84px] py-5 border-t-[1px] border-black mx-4 box-border">
      {/* Body */}
      <form
        onSubmit={e => e.preventDefault()}
        className="flex relative select-text"
      >
        <div className="bg-darkAccent relative rounded w-full">
          <p className="text-white">
            { buildUsersTypingMessage() } 
          </p>
          <input
            type="message"
            
            ref={inputRef}
            placeholder="Type something simple"
            className="caret-greenAccent bg-transparent text-white p-3 outline-0 w-full"

            onBlur={handleStoppedTyping}
            onFocus={handleStartedTyping}
            onChange={handleStartedTyping}

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
