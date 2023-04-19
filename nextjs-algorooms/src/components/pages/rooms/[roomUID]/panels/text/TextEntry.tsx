// Module imports
import React, { useState, useRef } from 'react';
import { BsFillSendFill } from 'react-icons/bs';
import { useUser } from '@auth0/nextjs-auth0/client';

// Interface imports
import { textEntryInterface } from './Interfaces';

export default ({ socket }: textEntryInterface) => {
  // Code
  const [message, setMessage] = useState('');
  const { isLoading, user, error } = useUser();


  // Send message
  const sendMessage = () => {
    //Check if the message is empty first
    if (message != '') {
      const name = isLoading || !user ? '': user.name || '';
      //emit the message to the server
      socket.emit('chat message', { message, name });
      //Reset message to black after sending.
      setMessage('');
    }
  };

  const handleSending = (e: any) => {
    if (e.key === 'Enter') sendMessage();
  };

  return (
    <section className="py-5 border-t-[1px] border-black mx-4">
      {/* Body */}
      <div className="flex relative select-text">
        <div className="bg-darkAccent relative w-full rounded overflow-hidden">
          <input
            value={message}
            placeholder="Type something simple"
            className="caret-greenAccent bg-transparent text-white p-3 outline-0"
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleSending}
          />
          <button onClick={sendMessage}>
            <BsFillSendFill className="absolute right-4 top-4 rotate-45" color="gray"/>
          </button>
        </div>
      </div>
    </section>
  );
};
