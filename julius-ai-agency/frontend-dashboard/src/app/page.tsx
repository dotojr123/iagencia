"use client";
import { useState, useEffect } from 'react';
import { checkHealth, dispatchTask } from '../services/api';

export default function Home() {
  const [status, setStatus] = useState<string>('Checking...');
  const [task, setTask] = useState('');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    checkHealth().then(data => {
      if (data) setStatus(`Online (v${data.version})`);
      else setStatus('Offline');
    });
  }, []);

  const handleDispatch = async () => {
    if (!task) return;
    setLoading(true);
    try {
      const res = await dispatchTask(task);
      setResult(res);
    } catch (e) {
      alert('Failed to dispatch task');
    }
    setLoading(false);
  };

  return (
    <main className="min-h-screen p-24 bg-gray-50 text-black">
      <h1 className="text-4xl font-bold mb-4">🦅 Jules AI Agency</h1>
      <div className="mb-8">
        <span className={`px-3 py-1 rounded-full text-white ${status.includes('Online') ? 'bg-green-500' : 'bg-red-500'}`}>
          Backend: {status}
        </span>
      </div>

      <div className="bg-white p-6 rounded-lg shadow-md max-w-2xl">
        <h2 className="text-2xl font-semibold mb-4">Dispatch a Mission</h2>
        <textarea
          className="w-full p-4 border rounded mb-4 text-black"
          rows={4}
          placeholder="Ex: Analyze the market trends for Electric Vehicles in 2026..."
          value={task}
          onChange={(e) => setTask(e.target.value)}
        />
        <button
          onClick={handleDispatch}
          disabled={loading}
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? 'Processing...' : 'Dispatch Agents'}
        </button>
      </div>

      {result && (
        <div className="mt-8 bg-white p-6 rounded-lg shadow-md max-w-2xl">
          <h3 className="text-xl font-bold mb-2">Mission Report</h3>
          <div className="bg-gray-100 p-4 rounded text-sm overflow-auto max-h-96">
            <pre>{JSON.stringify(result, null, 2)}</pre>
          </div>
        </div>
      )}
    </main>
  );
}
