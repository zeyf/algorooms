import React from 'react';

interface ContentInterface {
  children: React.ReactNode;
}

const Content = ({ children }: ContentInterface) => {
  return <div className="w-full h-[calc(100vh-64px)]">{children}</div>;
};

export default Content;
