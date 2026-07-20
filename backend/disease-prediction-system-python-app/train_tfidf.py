import os
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer


def train_tfidf():

    # Load doctor notes dataset
    df = pd.read_csv("../data/doctor_notes.csv") 

    # Combine text columns
    df["combined_text"] = (
        df["symptoms"].fillna("") + " " +
        df["doctor_notes"].fillna("")
    )

    # TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=500
    )

    vectorizer.fit(df["combined_text"])

    # Create directory if not exists
    os.makedirs("trained_models", exist_ok=True)

    # Save vectorizer
    joblib.dump(
        vectorizer,
        "trained_models/tfidf.pkl"
    )

    print("TF-IDF vectorizer saved successfully")


if __name__ == "__main__":
    train_tfidf()