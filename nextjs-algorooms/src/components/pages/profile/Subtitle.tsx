import React from 'react';

interface SubtitleInterface {
  text: string;
  alignment: string;
  color: string;
}

function Subtitle({ text, alignment, color }: SubtitleInterface) {
  return <h2 className={`text-${alignment} text-${color}`}>{text}</h2>;
}

export default Subtitle;
