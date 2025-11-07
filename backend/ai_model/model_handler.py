"""
Updated Model Handler - Works with Spam & Malware Models
Loads spam_model.pkl and spam_tfidf.pkl for text-based predictions
"""

import joblib
import numpy as np
import os

class ModelHandler:
    """Handles AI model loading and predictions"""
    
    def __init__(self, model_type="spam"):
        """
        Initialize model handler
        Args:
            model_type: "spam" or "malware"
        """
        self.model_type = model_type
        self.model = None
        self.tfidf = None
        self.feature_names = None
        self.load_model()
    
    def load_model(self):
        """Load the trained model from file"""
        try:
            if self.model_type == "spam":
                # Load spam model and vectorizer
                model_path = "ai_model/spam_model.pkl"
                tfidf_path = "ai_model/spam_tfidf.pkl"
                
                if not os.path.exists(model_path):
                    raise FileNotFoundError(f"Model file not found at {model_path}")
                
                self.model = joblib.load(model_path)
                self.tfidf = joblib.load(tfidf_path)
                
                print(f"✓ Spam model loaded successfully")
                
            elif self.model_type == "malware":
                # Load malware model
                model_path = "ai_model/malware_model.pkl"
                
                if not os.path.exists(model_path):
                    raise FileNotFoundError(f"Model file not found at {model_path}")
                
                self.model = joblib.load(model_path)
                print(f"✓ Malware model loaded successfully")
            
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    
    def predict_spam(self, text_input: str, numeric_feature: float = None) -> dict:
        """
        Make spam prediction
        Args:
            text_input: Email/message text
            numeric_feature: Not used for spam, but kept for API compatibility
        
        Returns:
            Dictionary with prediction results
        """
        try:
            # Convert text to TF-IDF features
            X_tfidf = self.tfidf.transform([text_input])
            
            # Get prediction and probability
            prediction = self.model.predict(X_tfidf)[0]
            probabilities = self.model.predict_proba(X_tfidf)[0]
            
            # Map to class names
            class_names = ["ham", "spam"]
            predicted_class = class_names[self.model.classes_.tolist().index(prediction)]
            
            # Confidence is probability of predicted class
            confidence = float(max(probabilities))
            
            # Create probability dictionary
            prob_dict = {
                class_names[i]: float(probabilities[i])
                for i in range(len(class_names))
            }
            
            result = {
                "predicted_class": predicted_class,
                "prediction_label": 0 if predicted_class == "ham" else 1,
                "confidence": confidence,
                "probabilities": prob_dict,
                "distribution": [int(prob_dict["ham"] * 100), int(prob_dict["spam"] * 100), 0],
                "history": {
                    "labels": ["Scan 1", "Scan 2", "Scan 3"],
                    "values": [0.65, 0.72, confidence]
                }
            }
            
            return result
        
        except Exception as e:
            raise Exception(f"Spam prediction error: {str(e)}")
    
    def predict_malware(self, features_dict: dict) -> dict:
        """
        Make malware prediction
        Args:
            features_dict: Dictionary of numeric features
        
        Returns:
            Dictionary with prediction results
        """
        try:
            import pandas as pd
            
            # Convert to DataFrame
            X = pd.DataFrame([features_dict])
            
            # Get prediction and probability
            prediction = self.model.predict(X)[0]
            probabilities = self.model.predict_proba(X)[0]
            
            # Map to class names
            class_names = ["benign", "malware"]
            predicted_class = class_names[int(prediction)]
            
            # Confidence
            confidence = float(max(probabilities))
            
            # Create probability dictionary
            prob_dict = {
                class_names[i]: float(probabilities[i])
                for i in range(len(class_names))
            }
            
            result = {
                "predicted_class": predicted_class,
                "prediction_label": int(prediction),
                "confidence": confidence,
                "probabilities": prob_dict,
                "distribution": [int(prob_dict["benign"] * 100), int(prob_dict["malware"] * 100), 0],
                "history": {
                    "labels": ["Scan 1", "Scan 2", "Scan 3"],
                    "values": [0.65, 0.72, confidence]
                }
            }
            
            return result
        
        except Exception as e:
            raise Exception(f"Malware prediction error: {str(e)}")
    
    def predict(self, text_input: str = None, numeric_feature: float = None) -> dict:
        """
        Generic predict method
        For spam: provide text_input
        For malware: provide numeric_feature as dict or text_input containing features
        """
        try:
            if self.model_type == "spam":
                if not text_input:
                    raise ValueError("text_input required for spam prediction")
                return self.predict_spam(text_input, numeric_feature)
            
            elif self.model_type == "malware":
                if not numeric_feature:
                    raise ValueError("numeric_feature required for malware prediction")
                
                # If numeric_feature is a string, try to parse it as dict
                if isinstance(numeric_feature, str):
                    import json
                    numeric_feature = json.loads(numeric_feature)
                
                return self.predict_malware(numeric_feature)
        
        except Exception as e:
            raise Exception(f"Prediction error: {str(e)}")


# Global instance
model_handler_spam = None
model_handler_malware = None

def get_spam_model():
    """Get or create the spam model handler instance"""
    global model_handler_spam
    if model_handler_spam is None:
        model_handler_spam = ModelHandler(model_type="spam")
    return model_handler_spam

def get_malware_model():
    """Get or create the malware model handler instance"""
    global model_handler_malware
    if model_handler_malware is None:
        model_handler_malware = ModelHandler(model_type="malware")
    return model_handler_malware

def get_model_handler(model_type="spam"):
    """Get model handler by type"""
    if model_type == "spam":
        return get_spam_model()
    elif model_type == "malware":
        return get_malware_model()
    else:
        raise ValueError(f"Unknown model type: {model_type}")