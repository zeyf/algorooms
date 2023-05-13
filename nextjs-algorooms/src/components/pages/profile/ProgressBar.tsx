// Module imports
import React from 'react';

// Interface
interface progressBarInterface {
  backgroundColor: string;
  accentColor: string;
  numerator: number;
  denominator: number;
  width: string;
  height: string;
}

const ProgressBar = ({
  backgroundColor,
  accentColor,
  numerator,
  denominator,
  width,
  height,
}: progressBarInterface) => {
  // Code

  const completionPercentage: number = Math.floor(
    (numerator / denominator) * 100
  );
  const completionComplement = 100 - completionPercentage;

  return (
    <div
      className={`w-${width} h-${height} ${backgroundColor} rounded-full overflow-hidden`}
    >
      <div
        className={`w-full h-${height} ${accentColor}`}
        style={{ width: `${completionComplement}%` }}
      ></div>
    </div>
  );
};

export default ProgressBar;
