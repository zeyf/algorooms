import React from 'react';

interface TitleInterface {
  text: string;
  alignment: string;
}

function Title({ text, alignment }: TitleInterface) {
  return <h1 className={`text-4xl text-${alignment}`}>{text}</h1>;
}

export default Title;
