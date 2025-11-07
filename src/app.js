import React, { useState } from 'react';
import './App.css';
import InputForm from './components/InputForm';
import Results from './components/results.js';
import { predict } from './services/api';

function App() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Function to handle form submission and communicate with the back-end
  const handleFormSubmit = async (formData) => {
    setLoading(true);
    setError('');
    try {
      const result = await predict(formData);
      setPrediction(result);
    } catch (err) {
      setError(err.message);
      console.error('API call failed:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cybersecurity AI Dashboard</h1>
        <p>Analyze potential threats using our AI model</p>
      </header>
      <main>
        <InputForm onSubmit={handleFormSubmit} loading={loading} />
        {error && <div className="error-message">Error: {error}</div>}
        <Results prediction={prediction} loading={loading} />
      </main>
    </div>
  );
}

export default App;