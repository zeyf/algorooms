// Module imports
import React from 'react'

// Interface
interface progressBarInterface {
  "backgroundColor": string,
  "accentColor": string,
  "numerator": number,
  "denominator": number,
  "width": string,
  "height": string,
};

const ProgressBar = ({ backgroundColor, accentColor, numerator, denominator, width, height } : progressBarInterface) => {
  
  // Code
  
  const percentage: number = Math.floor(numerator / denominator * 100);
  
  return (
    <div className={`w-${width} h-${height} rounded-full bg-${backgroundColor} overflow-x-hidden`}>
      <div
        className={`h-full bg-${accentColor}`}
        style={{ width: `${percentage}%`}}
      />
    </div>
  )
}

export default ProgressBar