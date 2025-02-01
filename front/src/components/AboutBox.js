// Inside your App.js or component where you want the about box

import React from "react";
import "./../styles/AboutBox.css"; // Import the CSS for About box

function AboutBox() {
  return (
      <div className="about-container">
          <div className="about-box">
              <p className="about-text">About</p>
              <div className="about-content">
                  <p>Szymon zrobił front</p>
                  <p>i generator haiku</p>
                  <p>dodał też redis</p>
                  <br/>
                  <p>Ania zrobiła</p>
                  <p>backend fast api</p>
                  <p>oraz routering</p>
                  <br/>
                  <p>Jasiu zebrał to</p>
                  <p>wszystko razem do kupy</p>
                  <p>i zrobił docker</p>
              </div>
          </div>
      </div>
  );
}

export default AboutBox;