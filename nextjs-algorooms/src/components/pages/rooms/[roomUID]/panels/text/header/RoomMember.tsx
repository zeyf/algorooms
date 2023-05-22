// Module imports
import React from 'react';

// Interface imports
import { roomMemberInterface } from './Interfaces';
import Link from 'next/link';

export default ({
  username,
  color
}: roomMemberInterface) => {

  // Use black text on light colors, white text on dark colors
  const blackOrWhiteText = () => {
    const r = parseInt(color.slice(1, 3), 16) / 255;
    const g = parseInt(color.slice(3, 5), 16) / 255;
    const b = parseInt(color.slice(5, 7), 16) / 255;
    const luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b;

    if (luminance > 0.5) {
      return "black";
    }
    return "white";
  }

  return (
    <Link
      className="text-white text-center px-2 py-1 flex flex-col rounded-lg"
    
      // Link to the username
      href={`/profile/${username}`}

      // Set-force the background color
      style={{
        backgroundColor: color,
        color: blackOrWhiteText()
      }}
    >
      { username }
    </Link>
  );
};
