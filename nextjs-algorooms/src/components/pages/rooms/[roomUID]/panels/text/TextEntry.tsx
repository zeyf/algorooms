// Module imports
import React, { useState } from 'react';
import { BsFillSendFill } from 'react-icons/bs';

// Interface imports
import { textEntryInterface } from './Interfaces';

export default ({}: textEntryInterface) => {
  // Code
  const [message, setMessage] = useState('');

  // Send message
  const sendMessage = () => {};

  const handleSending = (e: any) => {
    if (e.key === 'Enter') sendMessage();
  };

  return (
    <section className="py-5 border-t-[1px] border-black mx-4">
      {/* Body */}
      <div className="flex relative select-text">
        <div className="bg-darkAccent relative w-full rounded overflow-hidden">
          <input
            placeholder="Type something simple"
            className="caret-greenAccent bg-transparent text-white p-3 outline-0"
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleSending}
          />
          <button onClick={sendMessage}>
            <BsFillSendFill className="absolute right-4 top-4" color="gray" />
          </button>
        </div>
      </div>
    </section>
  );
};
