"""
Retrain Models for Backend - Simplified Version
This script retrains your spam and malware models using joblib (instead of pickle)
and saves them in a format compatible with Python 3.14
"""

import pandas as pd
import numpy as np
import joblib
import os
import warnings
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import ConvergenceWarning

# Silence warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

def clean_text(text):
    """Clean text data"""
    if not isinstance(text, str):
        return ""
    return text.strip().lower()

def main():
    print("=" * 60)
    print("RETRAINING MODELS FOR BACKEND")
    print("=" * 60)
    
    # Create models folder if it doesn't exist
    os.makedirs("ai_model", exist_ok=True)
    
    # ==================== SPAM DETECTION ====================
    print("\n[1/2] Training Spam Detection Model...")
    
    try:
        # Load spam dataset
        spam = pd.read_csv("data/interim/spam_clean.csv")
        
        X_spam = spam["text"]
        y_spam = spam["label"]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_spam, y_spam, test_size=0.2, random_state=42
        )
        
        # TF-IDF Vectorization
        tfidf = TfidfVectorizer(max_features=5000)
        X_train_tfidf = tfidf.fit_transform(X_train)
        X_test_tfidf = tfidf.transform(X_test)
        
        # Train Logistic Regression (best balance of speed and accuracy)
        spam_model = LogisticRegression(max_iter=1000, solver="lbfgs", random_state=42)
        spam_model.fit(X_train_tfidf, y_train)
        
        # Evaluate
        train_score = spam_model.score(X_train_tfidf, y_train)
        test_score = spam_model.score(X_test_tfidf, y_test)
        print(f"   ✓ Spam model trained")
        print(f"   ✓ Train accuracy: {train_score:.2%}")
        print(f"   ✓ Test accuracy: {test_score:.2%}")
        
        # Save using joblib (NOT pickle)
        joblib.dump(spam_model, "ai_model/spam_model.pkl", protocol=2)
        joblib.dump(tfidf, "ai_model/spam_tfidf.pkl", protocol=2)
        print(f"   ✓ Saved: ai_model/spam_model.pkl")
        print(f"   ✓ Saved: ai_model/spam_tfidf.pkl")
        
    except Exception as e:
        print(f"   ✗ Error training spam model: {e}")
        print("   ! Make sure you have data/interim/spam_clean.csv")
    
    # ==================== MALWARE DETECTION ====================
    print("\n[2/2] Training Malware Detection Model...")
    
    try:
        # Load malware dataset
        malware = pd.read_csv("data/interim/malware_clean.csv")
        
        # Drop hash column if it exists
        if "hash" in malware.columns:
            malware = malware.drop(columns=["hash"])
        
        X_malware = malware.drop(columns=["label"])
        y_malware = malware["label"].map({"malware": 1, "benign": 0})
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_malware, y_malware, test_size=0.2, random_state=42
        )
        
        # Train Random Forest
        malware_model = RandomForestClassifier(n_estimators=100, random_state=42)
        malware_model.fit(X_train, y_train)
        
        # Evaluate
        train_score = malware_model.score(X_train, y_train)
        test_score = malware_model.score(X_test, y_test)
        print(f"   ✓ Malware model trained")
        print(f"   ✓ Train accuracy: {train_score:.2%}")
        print(f"   ✓ Test accuracy: {test_score:.2%}")
        
        # Save using joblib
        joblib.dump(malware_model, "ai_model/malware_model.pkl", protocol=2)
        print(f"   ✓ Saved: ai_model/malware_model.pkl")
        
    except Exception as e:
        print(f"   ✗ Error training malware model: {e}")
        print("   ! Make sure you have data/interim/malware_clean.csv")
    
    print("\n" + "=" * 60)
    print("✓ MODEL RETRAINING COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()