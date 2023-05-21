// Module imports
import React from 'react';
import TextEntry from './TextEntry';
import TextFeed from './TextFeed';
import RoomMembers from './header/RoomMembers';

// Interface imports
import { textPanelInterface } from './Interfaces';

export default ({

}: textPanelInterface) => {
  // Code


  return (
    <section>
      {/* Body */}
      <div className='flex flex-col relative h-full -z-1'>
        <RoomMembers />
        <TextFeed />
        <TextEntry />
      </div>
    </section>
  );
};
