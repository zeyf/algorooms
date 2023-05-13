import React from 'react';

interface SubtitleInterface {
  text: string;
  alignment: string;
  color: string;
}

function Subtitle({ text, alignment, color }: SubtitleInterface) {
  return <h3 className={`text-lg text-${alignment} text-${color}`}>{text}</h3>;
}

export default Subtitle;
