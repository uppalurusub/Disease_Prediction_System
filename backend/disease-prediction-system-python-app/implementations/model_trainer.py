import os
import joblib
import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier




def train_model():

    # =========================
    # Load Dataset
    # =========================
    df = pd.read_csv("../data/patient_data.csv")

    # =========================
    # Combine Text Columns
    # =========================
    df["combined_text"] = (
        df["symptoms"].fillna("") + " " +
        df["doctor_notes"].fillna("")
    )

    # =========================
    # Numerical Features
    # =========================
    numerical_features = [
        "age",
        "bp",
        "glucose",
        "cholesterol",
        "bmi",
        "heart_rate",
        "oxygen_level"
    ]

    # =========================
    # Input Features
    # =========================
    X = df[numerical_features + ["combined_text"]]

    # =========================
    # Encode Labels
    # =========================
    label_encoder = LabelEncoder()

    y = label_encoder.fit_transform(df["target"])

    # =========================
    # Save Label Encoder
    # =========================
    os.makedirs("trained_models", exist_ok=True)

    joblib.dump(
        label_encoder,
        "trained_models/label_encoder.pkl"
    )

    # =========================
    # Preprocessing
    # =========================
    preprocessor = ColumnTransformer(
        transformers=[

            (
                "text",
                TfidfVectorizer(
                    stop_words="english",
                    max_features=500
                ),
                "combined_text"
            )

        ],
        remainder="passthrough"
    )

    # =========================
    # Ensemble Model
    # =========================
    ensemble_model = VotingClassifier(
        estimators=[

            (
                "lr",
                LogisticRegression(max_iter=1000)
            ),

            (
                "rf",
                RandomForestClassifier(
                    n_estimators=100
                )
            ),

            (
                "svm",
                SVC(probability=True)
            ),

            (
                "xgb",
                XGBClassifier(
                    eval_metric="mlogloss"
                )
            )

        ],
        voting="soft"
    )

    # =========================
    # Full Pipeline
    # =========================
    pipeline = Pipeline([

        (
            "preprocessor",
            preprocessor
        ),

        (
            "classifier",
            ensemble_model
        )

    ])

    # =========================
    # Train Test Split
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # =========================
    # MLflow
    # =========================
    mlflow.set_experiment(
        "Disease Prediction System"
    )

    with mlflow.start_run():

        # =====================
        # Train
        # =====================
        pipeline.fit(X_train, y_train)

        # =====================
        # Predict
        # =====================
        predictions = pipeline.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        # =====================
        # MLflow Logs
        # =====================
        mlflow.log_metric(
            "accuracy",
            accuracy
        )

        mlflow.sklearn.log_model(
            sk_model=pipeline,
            name="DiseasePredictionModel",
            serialization_format="pickle"
            
        )

        
        # =====================
        # Save Model
        # =====================
        joblib.dump(
            pipeline,
            "trained_models/ensemble_model.pkl"
        )

        print(f"Accuracy: {accuracy}")

        print(
            "Model saved successfully"
        )


if __name__ == "__main__":

    train_model()