import React, { useState, useEffect } from "react";
import { fetchHaikus, fetchQueueSize, clearQueue } from "./Api";
import HaikuDisplay from "./components/HaikuDisplay";
import QueueControls from "./components/QueueControls";
import "./styles/App.css";
import SakuraPetal from "./components/SakuraPetal";

function App() {
  const [haikus, setHaikus] = useState([]);
  const [queueSize, setQueueSize] = useState(0);
  const [loading, setLoading] = useState(false);

  const getHaikus = async (num) => {
    setLoading(true);
    const data = await fetchHaikus(num);
    setHaikus(data);
    setLoading(false);
  };

  useEffect(() => {
    const updateQueueSize = async () => {
      setQueueSize(await fetchQueueSize());
    };
    updateQueueSize();
    const interval = setInterval(updateQueueSize, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app-container">
      <SakuraPetal /> {/* Sakura Petals component */}
      <h1>Haiku Generator</h1>
      <p className="queue-size"><strong>Queue Size:</strong> {queueSize}</p>

      <QueueControls fetchHaikus={getHaikus} clearQueue={clearQueue} loading={loading} />
      <HaikuDisplay haikus={haikus} />
    </div>
  );
}

export default App;