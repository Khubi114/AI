from fastapi import HTTPException

def validate_input_text(text: str) -> bool:
    """Validate text input"""
    if not text or not text.strip():
        raise HTTPException(
            status_code=400,
            detail="Input text cannot be empty"
        )
    
    if len(text.strip()) < 10:
        raise HTTPException(
            status_code=400,
            detail="Input text must be at least 10 characters long"
        )
    
    if len(text) > 5000:
        raise HTTPException(
            status_code=400,
            detail="Input text cannot exceed 5000 characters"
        )
    
    return True

def validate_numeric_feature(value: float) -> bool:
    """Validate numeric feature"""
    if value < 0:
        raise HTTPException(
            status_code=400,
            detail="Numeric feature must be non-negative"
        )
    
    if value > 1000:
        raise HTTPException(
            status_code=400,
            detail="Numeric feature must be less than 1000"
        )
    
    return True