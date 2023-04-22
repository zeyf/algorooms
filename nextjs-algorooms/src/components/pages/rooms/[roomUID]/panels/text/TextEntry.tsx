// Module imports
import React, { useState, useRef, useContext, useEffect } from 'react';
import { BsFillSendFill } from 'react-icons/bs';
import { useUser } from '@auth0/nextjs-auth0/client';

// Interface imports
import { textEntryInterface } from './Interfaces';
import { RoomContext } from '@/contexts/RoomContextLayer';

export default ({
  socket
}: textEntryInterface) => {

  // For message state
  const [
    message,
    setMessage
  ] = useState("");

  // Get user information
  // Note, the /rooms/[roomUID] is auth protected
  const {
    user
  } = useUser();

  const {
    messages,
    setMessages,
    uid
  } = useContext(RoomContext);

  // Sends message to other users in the room
  const sendMessage = () => {

    //Check if the message is empty first
    if (message !== "") {

      //emit the message to the server

      // Store the payload for local client and socket room-connected clients
      const messagePayload = {
        message,
        username: user.name,
        timestamp: Date.now()
      };

      // Alter local client
      setMessages([
        ...messages,
        messagePayload
      ]);

      // Emit to the backend for socket room-connected clients to receive the message
      socket.emit("newChatMessage", messagePayload, uid);

      //Reset message to black after sending.
      setMessage("");
    }
  };

  useEffect(() => {

    // Listen for updates on the text chat and update it
    socket.on(
      "updateTextChat",
      newMessageData => setMessages([
        ...messages,
        newMessageData
      ])
    );
  
  // Listen for a change, also re-poll on send of a message from local client
  }, [ messages.length ]);

  return (
    <section className="py-5 border-t-[1px] border-black mx-4">
      {/* Body */}
      <form
        onSubmit={e => e.preventDefault()}
        className="flex relative select-text"
      >
        <div className="bg-darkAccent relative w-full rounded overflow-hidden">
          <input type="message"
            value={message}
            placeholder="Type something simple"
            className="caret-greenAccent bg-transparent text-white p-3 outline-0"
            onChange={e => setMessage(e.target.value)}
          />
          <button type="submit" onClick={e => {
            e.preventDefault();
            sendMessage();
          }}>
            <BsFillSendFill className="absolute right-4 top-4 rotate-45" color="gray" />
          </button>
        </div>
      </form>
    </section>
  );
};
