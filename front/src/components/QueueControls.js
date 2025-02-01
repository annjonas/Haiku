import React, { useState } from "react";
import "./../styles/QueueControls.css";

const QueueControls = ({ fetchHaikus, clearQueue, loading }) => {
  const [numHaikus, setNumHaikus] = useState(1);

  return (
    <div className="queue-controls">
      <input
        type="number"
        value={numHaikus}
        min="1"
        onChange={(e) => setNumHaikus(Number(e.target.value))}
      />
      <button onClick={() => fetchHaikus(numHaikus)} disabled={loading}>
        {loading ? "Loading..." : "Get Haikus"}
      </button>

      <button className="clear" onClick={clearQueue}>
        Clear Queue
      </button>
    </div>
  );
};

export default QueueControls;