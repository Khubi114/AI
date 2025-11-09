import React from 'react';
import BarChart from 'frontend/src/components/charts/barchar.js';
import LineChart from 'frontend/src/components/charts/linechart.js';
import PieChart from 'frontend/src/components/charts/piechart.js';

const Results = ({ prediction, loading }) => {
  if (loading) {
    return (
      <section className="results">
        <div className="loading">Analyzing data with AI model...</div>
      </section>
    );
  }

  if (!prediction) {
    return null;
  }

  return (
    <section className="results">
      <h2>Analysis Results</h2>
      
      <div className="prediction-summary">
        <h3>Prediction: <span className={`prediction ${prediction.class}`}>
          {prediction.predicted_class}
        </span></h3>
        <p>Confidence: <strong>{(prediction.confidence * 100).toFixed(2)}%</strong></p>
      </div>

      <div className="charts-container">
        <div className="chart-wrapper">
          <BarChart data={prediction} />
        </div>
        
        <div className="chart-wrapper">
          <LineChart history={prediction.history} />
        </div>
        
        <div className="chart-wrapper">
          <PieChart data={prediction} />
        </div>
      </div>

      <div className="export-options">
        <button 
          onClick={() => {
            const dataStr = JSON.stringify(prediction, null, 2);
            const dataBlob = new Blob([dataStr], { type: 'application/json' });
            const url = URL.createObjectURL(dataBlob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'prediction-results.json';
            link.click();
          }}
          className="export-btn"
        >
          Export Results as JSON
        </button>
      </div>
    </section>
  );
};

export default Results;