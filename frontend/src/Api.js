const API_URL = "http://localhost:5000";

export const fetchHaikus = async (numHaikus) => {
  try {
    const response = await fetch(`${API_URL}/haiku?number=${numHaikus}`);
    if (!response.ok) throw new Error("Failed to fetch haikus");
    const data = await response.json();
    return data.haiku_list;
  } catch (error) {
    console.error(error);
    return [];
  }
};

export const fetchQueueSize = async () => {
  try {
    const response = await fetch(`${API_URL}/haiku/qsize`);
    if (!response.ok) throw new Error("Failed to fetch queue size");
    const data = await response.json();
    return data.size;
  } catch (error) {
    console.error(error);
    return 0;
  }
};

export const clearQueue = async () => {
  try {
    await fetch(`${API_URL}/haiku`, { method: "DELETE" });
  } catch (error) {
    console.error(error);
  }
};