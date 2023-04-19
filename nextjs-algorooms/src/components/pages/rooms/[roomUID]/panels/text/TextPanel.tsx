// Module imports
import React from 'react';
import TextEntry from './TextEntry';
import TextFeed from './TextFeed';

// Interface imports
import { textPanelInterface } from './Interfaces';
import RoomMembers from './header/RoomMembers';

export default ({ socket }: textPanelInterface) => {
  // Code

  // DUMMY DATA
  const members = [
    { name: 'Khoi', color: 'bg-red-400' },
    { name: 'Zain', color: 'bg-green-400' },
    { name: 'John', color: 'bg-blue-400' },
    { name: 'Khoa', color: 'bg-yellow-400' },
    { name: 'James', color: 'bg-pink-400' },
  ];

  return (
    <section className="flex flex-col">
      {/* Body */}
      <RoomMembers members={members} />
      <TextFeed socket={socket}/>
      <TextEntry socket={socket} />
    </section>
  );
};
