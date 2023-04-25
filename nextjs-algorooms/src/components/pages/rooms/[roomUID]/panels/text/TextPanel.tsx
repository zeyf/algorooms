// Module imports
import React, { useContext, useEffect, useState } from 'react';
import TextEntry from './TextEntry';
import TextFeed from './TextFeed';

// Interface imports
import { textPanelInterface } from './Interfaces';
import RoomMembers from './header/RoomMembers';

export default ({

}: textPanelInterface) => {
  // Code


  return (
    <section className="flex flex-col">
      {/* Body */}
      <RoomMembers />
      <TextFeed />
      <TextEntry />
    </section>
  );
};
