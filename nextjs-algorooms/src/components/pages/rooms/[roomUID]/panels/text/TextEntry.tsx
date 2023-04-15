// Module imports
import React, { useState } from 'react';
import { BsFillSendFill } from 'react-icons/bs';

// Interface imports
import { textEntryInterface } from './Interfaces';

export default ({}: textEntryInterface) => {
  // Code
  const [message, setMessage] = useState('');

  // Send message
  const sendMessage = () => {
    //Check if the message is empty first
    if (message != '') {
      //Reset message to black after sending.
      setMessage('');
    }
  };

  const handleSending = (e: any) => {
    if (e.key === 'Enter') sendMessage();
  };

  return (
    <section className="m-5">
      {/* Body */}
      <div className="flex relative select-text">
        <div className="bg-darkAccent relative w-full rounded overflow-hidden">
          <input
            placeholder="Type something simple"
            className="caret-greenAccent bg-transparent text-white p-1 outline-0"
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleSending}
          />
          <button onClick={sendMessage}>
            <BsFillSendFill className="absolute right-1 top-2" color="gray" />
          </button>
        </div>
      </div>
    </section>
  );
};
