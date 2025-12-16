export const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function checkHealth() {
  try {
    const res = await fetch(`${API_URL}/`);
    if (!res.ok) throw new Error('Network response was not ok');
    return await res.json();
  } catch (error) {
    console.error("Health check failed:", error);
    return null;
  }
}

export async function dispatchTask(task: string, topic?: string) {
  try {
    const res = await fetch(`${API_URL}/agency/dispatch`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ task, topic }),
    });
    if (!res.ok) throw new Error('Task dispatch failed');
    return await res.json();
  } catch (error) {
    console.error("Dispatch failed:", error);
    throw error;
  }
}
