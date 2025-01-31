import React from "react";
import "./../styles/HaikuDisplay.css";

const HaikuDisplay = ({ haikus }) => {
  return (
    <div className="haiku-container">
      {haikus.map((haiku, index) => (
        <div key={index} className="haiku-card">
          <p>{haiku.line1}</p>
          <p>{haiku.line2}</p>
          <p>{haiku.line3}</p>
        </div>
      ))}
    </div>
  );
};

export default HaikuDisplay;