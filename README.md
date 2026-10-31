# Cybersecurity AI Dashboard

A full-stack web application that uses AI to detect spam and malware. Users submit text and a numeric value through a React interface, a FastAPI backend returns predictions, and the results are shown as interactive charts.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Frontend Components](#frontend-components)
- [Available Scripts](#available-scripts)
- [Responsive Design](#responsive-design)
- [Accessibility](#accessibility)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Features

- Input form with real-time validation
- Bar, line and pie charts with interactive features
- Responsive layout for desktop, tablet and mobile
- Live integration with the FastAPI backend
- Export of prediction results as JSON
- Clear error handling and user feedback
- WCAG 2.1 AA accessibility compliance

## Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | React, Chart.js, react-chartjs-2, Axios |
| Backend | Python 3.12+, FastAPI, Uvicorn |

## Project Structure

```text
AI/
├── backend/     # FastAPI server (app.py, requirements.txt)
├── frontend/    # React application
└── README.md
```

## Prerequisites

- Node.js 14 or higher
- npm 6 or higher (or yarn)
- Python 3.12 or higher ([python.org](https://www.python.org/downloads/)). During installation on Windows, tick **Add Python to PATH**.

## Getting Started

The backend must be running before the frontend can make predictions, so set it up first.

### 1. Backend

From the `backend` folder:

```bash
# Create a virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

You should see `(venv)` at the start of your command line once the environment is active. When the server is ready it prints:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

Keep this terminal open. To check that it works, open [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API documentation. Press `Ctrl + C` to stop the server.

**Next time**, you only need to activate the virtual environment and run `python app.py` again.

### 2. Frontend

From the `frontend` folder:

```bash
npm install
npm start
```

The app opens at [http://localhost:3000](http://localhost:3000) with hot-reload enabled.

Dependencies installed include `react` and `react-dom` (core framework), `chart.js` and `react-chartjs-2` (charts), and `axios` (API requests).

## Configuration

Create a `.env` file in the `frontend` folder:

```env
REACT_APP_API_BASE_URL=http://localhost:8000
REACT_APP_APP_NAME=Cybersecurity AI Dashboard
```

If you run the backend on a different port, update `REACT_APP_API_BASE_URL` to match.

## Usage

1. Start the backend, then the frontend (see [Getting Started](#getting-started)).
2. Open [http://localhost:3000](http://localhost:3000).
3. Enter some input text (minimum 10 characters).
4. Enter a numeric value (positive number).
5. Click **Analyze** to submit the data.
6. View the predictions and charts.
7. Click the export button to download the results as JSON.

## API Reference

### `POST /predict`

Submits data for AI analysis.

**Request**

```json
{
  "inputText": "User provided text for analysis",
  "numericFeature": 42.5
}
```

The frontend processes the response, updates all charts and shows an error message if the request fails. You can also test every endpoint from the interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## Frontend Components

| Component | Purpose |
| --- | --- |
| `InputForm` | Captures and validates input, shows errors and loading state, fully keyboard and screen reader accessible |
| `BarChart` | Prediction probabilities across threat categories |
| `LineChart` | Confidence trends over time |
| `PieChart` | Threat distribution percentages |
| `Results` | Displays predictions and charts in a responsive grid, with export |

## Available Scripts

Run these from the `frontend` folder.

| Command | Description |
| --- | --- |
| `npm start` | Start the development server |
| `npm run build` | Create an optimized production build in `build/` |
| `npm test` | Run the test runner in interactive watch mode |
| `npm run eject` | Expose the build configuration (irreversible) |

## Responsive Design

| Screen | Width | Layout |
| --- | --- | --- |
| Desktop | > 1200px | 3 columns |
| Tablet | 768px to 1199px | 2 columns |
| Mobile | < 768px | 1 column |

## Accessibility

- Semantic HTML structure
- ARIA labels and descriptions
- Keyboard navigation
- Screen reader compatibility
- Color contrast compliance
- Focus management

## Troubleshooting

**Backend**

| Problem | Solution |
| --- | --- |
| `python` not found | Install Python from [python.org](https://www.python.org/downloads/) and tick **Add Python to PATH** during installation |
| `ModuleNotFoundError` | Make sure the virtual environment is activated (you should see `(venv)` in the command line) |
| Port 8000 in use | Run `python -m uvicorn app:app --port 8001` and open [http://localhost:8001/docs](http://localhost:8001/docs). Update `REACT_APP_API_BASE_URL` in the frontend to match |
| Can't connect to `localhost:8000` | Check that the backend terminal is still running and shows `Uvicorn running on...`. If not, start it with `python app.py` |

**Frontend**

| Problem | Solution |
| --- | --- |
| App won't start | Run `npm cache clean --force`, delete `node_modules`, then run `npm install` again |
| Charts not displaying | Confirm `chart.js` and `react-chartjs-2` are installed and check the browser console for errors |
| API connection errors | Check the backend is running at `http://localhost:8000`, that CORS is configured in the backend, and that your network is working |
| Build errors | Update Node.js to the latest supported version and clear the build cache |

Tips: React Developer Tools and the browser's console and network tabs are the quickest way to inspect API calls.

## Contributing

1. Follow React hooks and best practices.
2. Keep a consistent code style with ESLint.
3. Make sure all components are accessible and responsive.
4. Test across multiple browsers and devices.
5. Update this README when you add features.

Performance notes: chart re-renders are memoized, state management is kept lean, and production builds use code splitting and lazy loading.
