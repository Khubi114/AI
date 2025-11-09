from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
import numpy as np

# Lifespan events to replace deprecated on_event
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting Cybersecurity AI Backend...")
    print("📍 API URL: http://localhost:8000")
    print("📚 Documentation: http://localhost:8000/docs")
    print("❤️  Health Check: http://localhost:8000/health")
    print("⏹️  Press Ctrl+C to stop the server")
    yield
    # Shutdown
    print("👋 Shutting down Cybersecurity AI Backend...")

app = FastAPI(
    title="Cybersecurity AI API",
    description="AI-powered spam and malware detection backend",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionRequest(BaseModel):
    inputText: str
    numericFeature: float

class PredictionResponse(BaseModel):
    predicted_class: str
    confidence: float
    probabilities: list
    distribution: list
    history: dict

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        print(f"🔍 Received request: {request.inputText[:50]}...")
        
        # Simulate AI model processing
        text_length = len(request.inputText)
        numeric_value = request.numericFeature
        
        # Mock AI prediction logic
        threat_score = min(1.0, (text_length * 0.01 + numeric_value * 0.1))
        
        # Determine threat classification
        if threat_score < 0.3:
            predicted_class = "Safe"
        elif threat_score < 0.7:
            predicted_class = "Suspicious"
        else:
            predicted_class = "Malicious"
        
        # Mock probabilities for different threat classes
        probabilities = [
            max(0, 1 - threat_score - 0.2),  # Safe probability
            max(0, 0.5 - abs(threat_score - 0.5)),  # Suspicious probability
            threat_score  # Malicious probability
        ]
        
        # Normalize probabilities to sum to 1
        total = sum(probabilities)
        probabilities = [p/total for p in probabilities]
        
        # Mock data distribution
        distribution = [60, 25, 15]  # Safe, Suspicious, Malicious
        
        # Mock historical data
        history = {
            "labels": ["10:00", "10:01", "10:02", "10:03"],
            "values": [0.2, 0.5, 0.3, threat_score]
        }
        
        print(f"🎯 Prediction: {predicted_class} with {threat_score:.2f} confidence")
        
        return PredictionResponse(
            predicted_class=predicted_class,
            confidence=threat_score,
            probabilities=probabilities,
            distribution=distribution,
            history=history
        )
    
    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {
        "message": "Cybersecurity AI API is running!",
        "status": "active",
        "endpoints": {
            "GET /": "This message",
            "GET /health": "Health check", 
            "POST /predict": "AI prediction endpoint"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Cybersecurity AI API"}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )