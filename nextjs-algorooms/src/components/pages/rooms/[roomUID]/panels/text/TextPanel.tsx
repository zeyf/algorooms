// Module imports
import React from 'react';
import TextEntry from './TextEntry';
import TextFeed from './TextFeed';

// Interface imports
import { textPanelInterface } from './Interfaces';

export default ({}: textPanelInterface) => {
  // Code

  return (
    <section>
      {/* Body */}
      <TextFeed />
      <TextEntry />
    </section>
  );
};
