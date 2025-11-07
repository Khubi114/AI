===========================================================
           CYBERSECURITY AI DASHBOARD - FRONTEND
===========================================================

A modern React.js frontend application for analyzing cybersecurity threats 
using AI-powered predictions. This application provides an intuitive interface 
for users to input data, view AI model predictions, and interact with 
comprehensive data visualizations.

===========================================================
FEATURES
===========================================================

- Interactive Data Input Form with real-time validation
- Multiple Chart Types (Bar, Line, Pie) with interactive features
- Responsive Design optimized for desktop, tablet, and mobile
- Real-time API Integration with FastAPI backend
- Export Functionality for prediction results
- Comprehensive Error Handling and user feedback
- Accessibility Compliance with WCAG 2.1 AA standards

===========================================================
PREREQUISITES
===========================================================

Before running this application, ensure you have the following installed:

- Node.js (version 14 or higher)
- npm (version 6 or higher) or yarn
- Backend API (FastAPI server running on http://localhost:8000)

===========================================================
INSTALLATION
===========================================================

1. Clone or Download the Project
   -------------------------------------------------------
   If using git:
       git clone <repository-url>
       cd cybersecurity-ai-dashboard/frontend

   Or navigate manually to your project directory:
       cd frontend

2. Install Dependencies
   -------------------------------------------------------
       npm install

   This installs:
   - react & react-dom (Core React framework)
   - chart.js & react-chartjs-2 (Data visualization)
   - axios (HTTP client for API communication)

===========================================================
RUNNING THE APPLICATION
===========================================================

DEVELOPMENT MODE
   -------------------------------------------------------
       npm start

   This will:
   - Start the development server
   - Open your browser at http://localhost:3000
   - Enable hot-reload for instant updates
   - Show detailed error messages and warnings

PRODUCTION BUILD
   -------------------------------------------------------
       npm run build

   Creates an optimized production build in the "build/" folder.

TESTING
   -------------------------------------------------------
       npm test

   Launches the test runner in interactive watch mode.

===========================================================
CONFIGURATION
===========================================================

ENVIRONMENT VARIABLES
   -------------------------------------------------------
   Create a ".env" file in the root directory and include:

       REACT_APP_API_BASE_URL=http://localhost:8000
       REACT_APP_APP_NAME=Cybersecurity AI Dashboard

API CONFIGURATION
   -------------------------------------------------------
   The application connects to a FastAPI backend running at:
       http://localhost:8000

   Ensure your backend is active before using prediction features.

===========================================================
COMPONENT OVERVIEW
===========================================================

InputForm Component
   -------------------------------------------------------
   - Captures and validates user input
   - Real-time validation and error display
   - Loading state management
   - Fully accessible (ARIA, keyboard navigation)

Visualization Components
   -------------------------------------------------------
   - BarChart: Displays prediction probabilities across threat categories
   - LineChart: Shows confidence trends over time
   - PieChart: Visualizes threat distribution percentages

Results Component
   -------------------------------------------------------
   - Displays AI model predictions and visual charts
   - Includes export functionality
   - Uses responsive grid layout

===========================================================
API INTEGRATION
===========================================================

Endpoints Used
   -------------------------------------------------------
   POST /predict  -> Submit data for AI analysis

   Example Request:
   {
       "inputText": "User provided text for analysis",
       "numericFeature": 42.5
   }

Response Handling
   -------------------------------------------------------
   The application processes responses from the backend and updates 
   all visualization components accordingly with error handling.

===========================================================
RESPONSIVE DESIGN
===========================================================

Breakpoints:
   - Desktop:  > 1200px (3-column layout)
   - Tablet:   768px - 1199px (2-column layout)
   - Mobile:   < 768px (1-column layout)

===========================================================
ACCESSIBILITY FEATURES
===========================================================

- Semantic HTML structure
- ARIA labels and descriptions
- Keyboard navigation support
- Screen reader compatibility
- Color contrast compliance
- Focus management

===========================================================
TROUBLESHOOTING
===========================================================

Common Issues
   -------------------------------------------------------
   Application won’t start:
       npm cache clean --force
       rm -rf node_modules
       npm install

   Charts not displaying:
       Ensure Chart.js and react-chartjs-2 are installed.
       Check browser console for errors.

   API connection errors:
       Verify backend server is active (http://localhost:8000)
       Check CORS settings in backend
       Confirm network connectivity

   Build errors:
       Update Node.js to the latest supported version
       Clear build cache:
           npm run build --silent

Development Tips
   -------------------------------------------------------
   - Use React Developer Tools for debugging
   - Check console and network tab for API inspection
   - Hot-reload enables fast feedback during development

===========================================================
PERFORMANCE OPTIMIZATION
===========================================================

- Memoization for preventing unnecessary chart re-renders
- Efficient React state management
- Code splitting for production
- Optimized bundle size
- Lazy loading support

===========================================================
CONTRIBUTING
===========================================================

When contributing:

1. Follow React hooks and best practices
2. Maintain consistent code style using ESLint
3. Ensure all components are accessible and responsive
4. Test across multiple browsers and devices
5. Update this README for any new features

===========================================================
NPM SCRIPTS OVERVIEW
===========================================================

   npm start       -> Start development server
   npm run build   -> Create production build
   npm test        -> Run test suite
   npm run eject   -> Expose configuration (irreversible)

===========================================================
USAGE EXAMPLE
===========================================================

1. Start the application:
       npm start
2. Open your browser at:
       http://localhost:3000
3. Enter input text (minimum 10 characters)
4. Provide a numeric value (positive number)
5. Click "Analyze" to submit data
6. View predictions and charts
7. Export results as JSON using the export button

===========================================================
SUPPORT
===========================================================

For technical help:

1. Check browser console for errors
2. Verify dependencies are installed
3. Ensure backend API is running
4. Review configuration steps in this README