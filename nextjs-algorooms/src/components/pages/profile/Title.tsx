import React from 'react';

interface TitleInterface {
  text: string;
  alignment: string;
  color: string;
}

function Title({ text, alignment, color }: TitleInterface) {
  return <h1 className={`text-5xl text-${alignment} text-${color}`}>{text}</h1>;
}

export default Title;
