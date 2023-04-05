import React from 'react';

interface SubtitleInterface {
  text: string;
  alignment: string;
}

function Subtitle({ text }: SubtitleInterface) {
  return <h3>{text}</h3>;
}

export default Subtitle;
