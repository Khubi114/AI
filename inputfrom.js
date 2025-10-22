import React, { useState } from 'react';

const InputForm = ({ onSubmit, loading }) => {
  const [formData, setFormData] = useState({
    inputText: '',
    numericFeature: '',
  });
  const [errors, setErrors] = useState({});

  // Validation rules
  const validateForm = () => {
    const newErrors = {};
    if (!formData.inputText.trim()) {
      newErrors.inputText = 'Input text is required.';
    } else if (formData.inputText.length < 10) {
      newErrors.inputText = 'Input text must be at least 10 characters long.';
    }

    if (!formData.numericFeature || isNaN(formData.numericFeature) || formData.numericFeature < 0) {
      newErrors.numericFeature = 'Please enter a valid positive number.';
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      onSubmit(formData);
    }
  };

  return (
    <section className="input-form">
      <h2>Submit Data for Analysis</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="inputText">Text Input:</label>
          <textarea
            id="inputText"
            name="inputText"
            value={formData.inputText}
            onChange={handleChange}
            placeholder="Enter text to analyze..."
            rows="4"
          />
          {errors.inputText && <span className="error">{errors.inputText}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="numericFeature">Numeric Feature:</label>
          <input
            type="number"
            id="numericFeature"
            name="numericFeature"
            value={formData.numericFeature}
            onChange={handleChange}
            placeholder="Enter a number"
            step="0.01"
          />
          {errors.numericFeature && <span className="error">{errors.numericFeature}</span>}
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Processing...' : 'Analyze'}
        </button>
      </form>
    </section>
  );
};

export default InputForm;