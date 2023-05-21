// Module imports
import React, { useRef } from 'react';
import { BsFillSendFill } from 'react-icons/bs';

// Interface imports
import { textEntryInterface } from './Interfaces';
import { TextChatMessage, useMutation, useOthers, useSelf, useUpdateMyPresence } from '../../../../../../../liveblocks.config';

export default ({

}: textEntryInterface) => {

  // Take a reference to the input element used to type text chat messages
  const inputRef = useRef(null);

  // Get self presence
  const myPresence = useSelf(me => me.presence);

  // Get others' presence
  const others = useOthers();

  // Filter out others' by who is typing
  // Potentially in-efficient and slow to update, best practice may be useOthersMapped hook
  const othersTyping = others.filter(other => other.presence.isTypingMessage);

  // Used to update self presence
  const updatePresence = useUpdateMyPresence();

  // Used to add a message to the room storage's messages LiveList<TextChatMessage>
  const handleTextChatMessageAdd = useMutation(({
    storage,
    setMyPresence
  }, event, MYPRESENCE) => {

    // Prevent the default submission and refresh of the page
    event.preventDefault();
    
    // Create the object for the new message based on the TextChatMessage type, passing presence colors, the message, and the current timestamp
    const newMessage:TextChatMessage = {
      username: MYPRESENCE.username,
      color: MYPRESENCE.color,
      message: inputRef.current.value,
      timestamp: Date.now()
    };
    
    // Get the LiveList<TextChatMessage> and add a new message to it -- it will automatically update as it has CRDT built-in
    storage.get("messages").push(newMessage);

    // Update self presence to not be typing
    setMyPresence({
      ...MYPRESENCE,
      isTypingMessage: false
    });

    // Reset the input value to empty string via the reference
    inputRef.current.value = "";

  }, [  ]);

  // Update self presence to reflect typing onChange or onFocus of the input element
  const handleStartedTyping = () => !myPresence.isTypingCode && updatePresence({
    ...myPresence,
    isTypingMessage: true
  });

  // Update self presence to reflect typing onBlur (loss of focus) of the input element
  const handleStoppedTyping = () => updatePresence({
    ...myPresence,
    isTypingMessage: false
  });

  // Used to create the message as other users are typing
  const buildUsersTypingMessage = () => {

    // Display nothing if no one is typing
    if (othersTyping.length === 0)
      return "";
    
    // Display the username if only one user is typing
    else if (othersTyping.length === 1)
      return `${othersTyping[0].presence.username} is typing...`;

    // Display that several users are typing if more than one user is typing
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
