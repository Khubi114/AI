import React, { useState } from 'react';
import './App.css';
import InputForm from './components/InputForm';
import Results from './components/Results';

function App() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Function to handle form submission and communicate with the back-end
  const handleFormSubmit = async (formData) => {
    setLoading(true);
    setError('');
    setPrediction(null);
    
    try {
      console.log('📤 Sending to backend:', formData);
      
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const result = await response.json();
      console.log('📥 Received from backend:', result);
      setPrediction(result);
      
    } catch (err) {
      console.error('❌ API call failed:', err);
      setError(err.message || 'Failed to connect to backend');
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