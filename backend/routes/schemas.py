from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    """Schema for prediction request"""
    inputText: str = Field(..., min_length=10, description="Text to analyze")
    numericFeature: float = Field(..., ge=0, description="Numeric feature value")
    
    class Config:
        json_schema_extra = {
            "example": {
                "inputText": "This is a suspicious email message",
                "numericFeature": 42.5
            }
        }

class PredictionResponse(BaseModel):
    """Schema for prediction response"""
    predicted_class: str
    prediction_label: int
    confidence: float
    probabilities: dict
    distribution: list
    history: dict