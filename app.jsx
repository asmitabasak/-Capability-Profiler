import { useState } from 'react';

function App() {
  const [response, setResponse] = useState(null);

  const sendData = async () => {
    const res = await fetch('http://localhost:8000/api/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: "Sample", value: 42 })
    });
    const data = await res.json();
    setResponse(data);
  };

  return (
    <div>
      <h1>Full Stack Agent</h1>
      <button onClick={sendData}>Test Backend Connection</button>
      {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
    </div>
  );
}

export default App;
