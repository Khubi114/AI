BACKEND SETUP - QUICK START
====================================================================

WHAT IS THIS?
The AI backend that detects spam and malware. Website sends data here, 
gets predictions back.

====================================================================

REQUIREMENTS
- Python 3.12 or higher (download from python.org)
- backend.zip (extract it first)

====================================================================

SETUP (First Time Only)

Step 1: Extract and Open Terminal
- Unzip backend.zip
- Open Command Prompt/Terminal in the backend folder

Step 2: Create Virtual Environment
python -m venv venv

Step 3: Activate It

WINDOWS:
venv\Scripts\activate

MAC/LINUX:
source venv/bin/activate

You should see (venv) at the start of your command line

Step 4: Install Packages
pip install -r requirements.txt

====================================================================

RUN THE BACKEND

python app.py

Wait for this message:
INFO:     Uvicorn running on http://127.0.0.1:8000

KEEP THIS TERMINAL OPEN!

====================================================================

TEST IT

Open browser: http://localhost:8000/docs

You will see interactive API documentation. Click endpoints to test.

====================================================================

STOP THE BACKEND

Press Ctrl + C in the terminal

====================================================================

NEXT TIME

Just do this:
1. Open terminal in backend folder
2. Run: venv\Scripts\activate (Windows) or source venv/bin/activate (Mac/Linux)
3. Run: python app.py
4. Open: http://localhost:8000/docs

====================================================================

TROUBLESHOOTING

PROBLEM: python not found
SOLUTION: Install Python from python.org
          Make sure to check "Add Python to PATH" during install

PROBLEM: ModuleNotFoundError
SOLUTION: Make sure (venv) is activated (should see it in command line)

PROBLEM: Port 8000 in use
SOLUTION: Run: python -m uvicorn app:app --port 8001
          Then open: http://localhost:8001/docs

PROBLEM: Can't connect to localhost:8000
SOLUTION: Check the terminal - backend should be running
          You should see: INFO: Uvicorn running on...
          If not, start it with: python app.py

====================================================================

THAT'S IT!

Backend is ready. Works with React frontend for full application.

====================================================================