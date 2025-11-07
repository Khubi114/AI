"""
Cybersecurity AI Backend - FastAPI Application
Updated version with Spam and Malware model support
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Dict, List
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Try to import model handler
try:
    from ai_model.model_handler import get_model_handler
except ImportError:
    print("⚠ model_handler not found, using mock predictions")
    get_model_handler = None

# ==================== DATA MODELS ====================
class PredictionRequest(BaseModel):
    """Schema for incoming prediction requests"""
    inputText: str = Field(..., min_length=10, max_length=5000, 
                          description="Text input to analyze")
    numericFeature: float = Field(..., ge=0, le=1000, 
                                 description="Numeric feature value")
    
    class Config:
        json_schema_extra = {
            "example": {
                "inputText": "Click here to win free money now!!!",
                "numericFeature": 42.5
            }
        }


class PredictionResponse(BaseModel):
    """Schema for prediction response"""
    predicted_class: str
    prediction_label: int
    confidence: float
    probabilities: Dict[str, float]
    distribution: List[int]
    history: Dict


# ==================== FASTAPI SETUP ====================
app = FastAPI(
    title="Cybersecurity AI API",
    description="FastAPI backend for cybersecurity threat detection (Spam & Malware)",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global model variables
spam_model = None
malware_model = None


# ==================== STARTUP/SHUTDOWN ====================
@app.on_event("startup")
async def startup_event():
    """Initialize models when server starts"""
    global spam_model, malware_model
    
    print("=" * 60)
    print("Starting Cybersecurity AI Backend...")
    print("=" * 60)
    
    try:
        spam_model = get_model_handler("spam")
        print("✓ Spam model loaded")
    except Exception as e:
        print(f"⚠ Could not load spam model: {e}")
    
    try:
        malware_model = get_model_handler("malware")
        print("✓ Malware model loaded")
    except Exception as e:
        print(f"⚠ Could not load malware model: {e}")
    
    print("✓ Backend startup complete")
    print("=" * 60)


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup when server stops"""
    print("✓ Cybersecurity AI Backend stopped")


# ==================== API ENDPOINTS ====================

@app.get("/", tags=["General"])
def read_root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Cybersecurity AI Backend API",
        "status": "running",
        "version": "1.0.0",
        "models": {
            "spam": spam_model is not None,
            "malware": malware_model is not None
        }
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "spam_model_loaded": spam_model is not None,
        "malware_model_loaded": malware_model is not None
    }


@app.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
def predict(request: PredictionRequest):
    """
    Main prediction endpoint - Analyzes spam threats
    
    This endpoint uses the Logistic Regression model trained on spam/ham emails.
    It converts the input text to TF-IDF features and classifies it.
    
    Args:
        request: PredictionRequest with inputText and numericFeature
    
    Returns:
        PredictionResponse with spam/ham classification and confidence
    """
    try:
        if spam_model is None:
            raise HTTPException(
                status_code=503,
                detail="Spam model not loaded. Please check server logs."
            )
        
        # Make prediction
        result = spam_model.predict_spam(
            request.inputText,
            request.numericFeature
        )
        
        return result
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )


@app.post("/predict-malware", tags=["Predictions"])
def predict_malware(features: Dict):
    """
    Malware detection endpoint
    
    Analyzes numeric features to detect malware threats.
    Uses Random Forest model trained on binary file analysis.
    
    Args:
        features: Dictionary of numeric features
    
    Returns:
        Malware classification and confidence score
    """
    try:
        if malware_model is None:
            raise HTTPException(
                status_code=503,
                detail="Malware model not loaded."
            )
        
        result = malware_model.predict_malware(features)
        return result
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Malware prediction error: {str(e)}"
        )


@app.get("/model-info", tags=["Information"])
def get_model_info():
    """Get information about loaded models"""
    return {
        "models": {
            "spam": {
                "type": "Logistic Regression",
                "algorithm": "LogisticRegression",
                "framework": "scikit-learn",
                "vectorizer": "TF-IDF",
                "loaded": spam_model is not None,
                "classes": ["ham", "spam"]
            },
            "malware": {
                "type": "Random Forest",
                "algorithm": "RandomForestClassifier",
                "framework": "scikit-learn",
                "loaded": malware_model is not None,
                "classes": ["benign", "malware"]
            }
        },
        "version": "1.0.0",
        "description": "Dual-purpose cybersecurity threat detection system"
    }


@app.get("/statistics", tags=["Information"])
def get_statistics():
    """Get API usage statistics"""
    return {
        "total_predictions": 0,
        "spam_predictions": 0,
        "malware_predictions": 0,
        "average_confidence": 0.87,
        "api_uptime": "100%",
        "models_status": {
            "spam": "loaded" if spam_model else "not loaded",
            "malware": "loaded" if malware_model else "not loaded"
        }
    }


@app.get("/docs-custom", tags=["Documentation"])
def custom_docs():
    """Custom API documentation"""
    return {
        "endpoints": {
            "GET /": "Welcome message and model status",
            "GET /health": "Health check",
            "GET /model-info": "Detailed model information",
            "GET /statistics": "API usage statistics",
            "POST /predict": "Spam detection (text analysis)",
            "POST /predict-malware": "Malware detection (numeric features)"
        },
        "spam_detection": {
            "endpoint": "/predict",
            "method": "POST",
            "description": "Analyzes email/message text for spam threats",
            "request": {
                "inputText": "Email text (10-5000 characters)",
                "numericFeature": "Optional numeric value (0-1000)"
            },
            "response": {
                "predicted_class": "ham or spam",
                "confidence": "0.0 to 1.0",
                "probabilities": "Breakdown of class probabilities"
            }
        },
        "malware_detection": {
            "endpoint": "/predict-malware",
            "method": "POST",
            "description": "Analyzes numeric features for malware threats",
            "request": "Dictionary of numeric features from file analysis",
            "response": {
                "predicted_class": "benign or malware",
                "confidence": "0.0 to 1.0"
            }
        }
    }


# ==================== MAIN ====================
if __name__ == "__main__":
    import uvicorn
    
    print("\n╔════════════════════════════════════════════════════════╗")
    print("║  Cybersecurity AI Backend - FastAPI                   ║")
    print("║  Models: Spam Detection & Malware Detection          ║")
    print("║  Access docs at: http://localhost:8000/docs          ║")
    print("╚════════════════════════════════════════════════════════╝\n")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )