// src/components/SakuraPetals.js
import React, { useEffect } from "react";
import "./../styles/SakuraPetal.css";

const SakuraPetals = () => {
  useEffect(() => {
    // Create petals dynamically
    const petalContainer = document.querySelector(".sakura-petal-container");

    // Generate 50 petals
    for (let i = 0; i < 50; i++) {
      const petal = document.createElement("div");
      petal.classList.add("sakura-petal");

      // Randomize horizontal position and size for variation
      petal.style.left = `${Math.random() * 100}vw`;
      petal.style.animationDuration = `${Math.random() * (6 - 4) + 4}s`; // Randomize duration
      petal.style.animationDelay = `${Math.random() * 5}s`; // Random delay to make it more natural

      petalContainer.appendChild(petal);
    }

    // Cleanup function to remove petals when component unmounts
    return () => {
      petalContainer.innerHTML = "";
    };
  }, []);

  return <div className="sakura-petal-container"></div>;
};

export default SakuraPetals;