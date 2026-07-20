# 🩺 Disease Prediction System (Python)

A Machine Learning-powered Disease Prediction System built using **Python**, **FastAPI**, **Scikit-Learn**, **XGBoost**, and **MLflow**. The system predicts the most probable disease based on patient vitals, laboratory values, symptoms, and doctor notes using an ensemble learning approach.

---

# 📌 Project Overview

The Disease Prediction System leverages machine learning techniques to assist healthcare professionals by predicting diseases from structured and unstructured patient information.

The application combines:

- Numerical clinical features
- Patient symptoms
- Doctor notes
- Ensemble Machine Learning
- TF-IDF Text Vectorization
- REST API using FastAPI
- MLflow Experiment Tracking

The project demonstrates an end-to-end ML workflow including:

- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Experiment tracking
- Model persistence
- Prediction API

---

# 🚀 Features

- Disease Prediction API
- Ensemble Machine Learning Model
- Text + Numerical Feature Processing
- TF-IDF Feature Extraction
- MLflow Experiment Tracking
- FastAPI REST Services
- Confidence Score Prediction
- Label Encoding
- Modular Architecture
- Production Ready Structure

---

# 🏗️ Project Structure

```

disease-prediction-system-python-app/
│
├── implementations/
│ ├── disease_predictor.py
│ ├── ensemble_model.py
│ ├── mlflow_tracker.py
│ └── model_trainer.py
│
├── models/
│ └── request_models.py
│
├── routers/
│ └── prediction_router.py
│
├── services/
│ └── prediction_service.py
│
├── trained_models/
│ ├── ensemble_model.pkl
│ ├── label_encoder.pkl
│ └── tfidf.pkl
│
├── utils/
│ └── logger.py
│
├── mlruns/
├── mlflow.db
├── train_tfidf.py
├── main.py
└── README.md

⚙️ Technology Stack
Category	Technology
Language	Python 3.x
API Framework	FastAPI
ML Library	Scikit-Learn
Boosting	XGBoost
Text Processing	TF-IDF Vectorizer
Experiment Tracking	MLflow
Model Serialization	Joblib
Data Processing	Pandas
Validation	Pydantic
🧠 Machine Learning Pipeline

The application follows the complete ML lifecycle.

Patient Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ├── Numerical Features
        └── Text Features
                │
                ▼
         TF-IDF Vectorization
                │
                ▼
      Ensemble Voting Classifier
                │
                ▼
      Disease Prediction
                │
                ▼
       REST API Response
📊 Input Features
Numerical Features
Age
Blood Pressure
Glucose
Cholesterol
BMI
Heart Rate
Oxygen Level
Text Features
Symptoms
Doctor Notes
🤖 Machine Learning Models

The project uses a Soft Voting Ensemble Classifier consisting of multiple machine learning algorithms.

Included models:

Logistic Regression
Random Forest Classifier
Support Vector Machine (SVM)
XGBoost Classifier

The ensemble combines the predictions of all models to improve accuracy and robustness.

📝 Feature Engineering

The system combines structured and unstructured healthcare information.

Structured Features
Age
BP
Glucose
Cholesterol
BMI
Heart Rate
Oxygen Level
Unstructured Features
Symptoms
+
Doctor Notes
        │
        ▼
Combined Text
        │
        ▼
TF-IDF Vectorization
📈 Model Training

The training pipeline performs:

Dataset Loading
Label Encoding
Text Vectorization
Feature Transformation
Train/Test Split
Ensemble Model Training
Accuracy Evaluation
MLflow Logging
Model Serialization
📦 Saved Models

After training, the following artifacts are generated:

trained_models/

ensemble_model.pkl
label_encoder.pkl
tfidf.pkl
📊 MLflow Integration

The project includes MLflow experiment tracking.

Tracked information includes:

Experiment Name
Model Parameters
Accuracy
Trained Model
Artifacts

Start MLflow UI:

mlflow ui

Open:

http://localhost:5000
🚀 API Endpoints
Predict Disease
POST
/predict/
Request Body
{
  "age": 45,
  "bp": 130,
  "glucose": 110,
  "cholesterol": 210,
  "bmi": 28.5,
  "heart_rate": 82,
  "oxygen_level": 98,
  "symptoms": "fever cough fatigue",
  "doctor_notes": "patient reports breathing difficulty"
}
Response
{
  "prediction": "Pneumonia",
  "confidence": 0.9635
}
▶️ Installation
Clone Repository
git clone https://github.com/yourusername/disease-prediction-system.git
cd disease-prediction-system-python-app
Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux/Mac

python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
▶️ Run the API
uvicorn main:app --reload

Application

http://localhost:8000

Swagger UI

http://localhost:8000/docs

ReDoc

http://localhost:8000/redoc
🏋️ Train the Model

Run

python implementations/model_trainer.py

The training process will:

Train the ensemble model
Evaluate accuracy
Log metrics to MLflow
Save trained models
📊 Prediction Workflow
Client Request
        │
        ▼
FastAPI Router
        │
        ▼
Prediction Service
        │
        ▼
Disease Predictor
        │
        ▼
Load Trained Model
        │
        ▼
Prediction
        │
        ▼
Confidence Score
        │
        ▼
JSON Response
📂 Architecture
FastAPI
    │
    ▼
Router
    │
    ▼
Service Layer
    │
    ▼
Prediction Engine
    │
    ▼
Trained Ensemble Model
    │
    ▼
Prediction Response
🔒 Production Features
Modular Architecture
FastAPI REST API
Pydantic Validation
Ensemble Learning
MLflow Tracking
Saved Models
Confidence Score
Scalable Design
Production Deployment Ready
📈 Future Enhancements
Deep Learning Models
Explainable AI (SHAP/LIME)
Docker Support
Kubernetes Deployment
CI/CD Pipeline
JWT Authentication
Database Integration
Batch Prediction API
Model Versioning
Real-time Monitoring
Drift Detection
Automated Retraining
Cloud Deployment (AWS/Azure/GCP)
📚 Learning Objectives

This project demonstrates:

Machine Learning Pipeline Development
Healthcare AI Applications
FastAPI Development
Ensemble Learning
Natural Language Processing (TF-IDF)
MLflow Experiment Tracking
Model Deployment
REST API Development
Production ML Best Practices
👨‍💻 Author

Developed as an end-to-end Machine Learning project demonstrating healthcare disease prediction using modern Python technologies, FastAPI, Scikit-Learn, XGBoost, and MLflow.

📄 License

This project is intended for educational, research, and demonstration purposes. Please ensure compliance with healthcare data privacy regulations before using real patient data in production.