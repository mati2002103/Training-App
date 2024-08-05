// frontend/src/App.js
import React, { useEffect, useState } from 'react';

function App() {
  const [plan, setPlan] = useState(null);

  useEffect(() => {
    fetch('/api/generate_plan')
      .then(response => response.json())
      .then(data => setPlan(data));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Workout Plan</h1>
        {plan && (
          <pre>{JSON.stringify(plan, null, 2)}</pre>
        )}
      </header>
    </div>
  );
}

export default App;
