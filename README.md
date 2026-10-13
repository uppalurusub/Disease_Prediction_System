# 🏥 Disease Prediction System

> An end-to-end AI-powered Disease Prediction System built using Machine Learning, FastAPI, React TypeScript, Streamlit, and MLflow.

---

# 📌 Overview

The Disease Prediction System predicts the most probable disease by combining structured clinical information with unstructured medical text.

The application demonstrates a production-ready Machine Learning architecture including:

- Disease Prediction
- Ensemble Machine Learning
- TF-IDF Text Processing
- Doctor Notes Analysis
- FastAPI REST APIs
- React TypeScript Frontend
- Streamlit Client
- MLflow Experiment Tracking
- Model Management
- Production Deployment Ready Architecture

---

# Architecture

![alt text](image.png)

---

# Project Structure

```
Disease_Prediction_System
│
├── backend
│   ├── data
│   │   ├── patient_data.csv
│   │   └── doctor_notes.csv
│   │
│   ├── disease-prediction-system-python-app
│   │   ├── implementations
│   │   ├── routers
│   │   ├── services
│   │   ├── models
│   │   ├── trained_models
│   │   ├── utils
│   │   ├── mlruns
│   │   ├── mlflow.db
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── sample_request.json
│
├── ui
│   ├── app.py
│   ├── api_client.py
│   ├── config.py
│   │
│   └── reactjs
│       └── disease-prediction-system-react-app
│
├── README.md
└── requirements.txt
```

---

# Features

## Backend

- FastAPI REST APIs
- Modular architecture
- ML model loading
- Ensemble prediction
- TF-IDF text processing
- Structured clinical feature processing
- Doctor notes analysis
- MLflow integration
- Logging
- CORS support

---

## Machine Learning

The system combines multiple information sources.

### Structured Features

- Age
- Blood Pressure
- Glucose
- Cholesterol
- BMI
- Heart Rate
- Oxygen Level

### Unstructured Features

- Symptoms
- Doctor Notes

### ML Components

- TF-IDF Vectorizer
- Ensemble Model
- Label Encoder

---

## Frontend

Built using

- React 19
- TypeScript
- Vite
- Axios

Features

- Disease Prediction Form
- API Integration
- Loading Indicators
- Prediction Result Display

---

## Streamlit UI

The repository also includes a lightweight Streamlit interface for rapid testing.

Features

- User-friendly prediction form
- API communication
- JSON response visualization

---

# Technology Stack

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Machine Learning

- Scikit-learn
- TF-IDF
- Ensemble Learning
- MLflow

---

## Frontend

- React
- TypeScript
- Vite
- Axios

---

## Data

- CSV Dataset
- Patient Records
- Doctor Notes

---

# REST API

## Predict Disease

```
POST /predict/
```

### Request

```json
{
  "age": 45,
  "bp": 130,
  "glucose": 150,
  "cholesterol": 220,
  "bmi": 28,
  "heart_rate": 82,
  "oxygen_level": 97,
  "symptoms": "fever cough fatigue",
  "doctor_notes": "Patient reports persistent cough and elevated temperature."
}
```

---

### Response

```json
{
  "predicted_disease": "Pneumonia",
  "confidence": 0.94
}
```

---

# Backend Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Disease_Prediction_System.git

cd Disease_Prediction_System
```

---

## Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Start FastAPI

```bash
cd backend/disease-prediction-system-python-app

uvicorn main:app --reload
```

API Documentation

```
http://localhost:8000/docs
```

---

# React Frontend

Navigate

```bash
cd ui/reactjs/disease-prediction-system-react-app
```

Install

```bash
npm install
```

Run

```bash
npm run dev
```

Application

```
http://localhost:5173
```

---

# Streamlit UI

Navigate

```bash
cd ui
```

Install

```bash
pip install -r ../requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# MLflow

Launch MLflow UI

```bash
mlflow ui
```

or

```bash
mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns \
--host 0.0.0.0 \
--port 5000
```

Open

```
http://localhost:5000
```

---

# Model Pipeline

```
Patient Data
      │
      ▼
Validation
      │
      ▼
Feature Engineering
      │
      ├──────────────┐
      │              │
Structured      Doctor Notes
Features            │
      │             ▼
      │        TF-IDF
      │             │
      └──────┬──────┘
             ▼
      Ensemble Model
             ▼
 Disease Prediction
             ▼
 REST Response
```

---

# Request Model

| Field | Type |
|----------|---------|
| age | int |
| bp | float |
| glucose | float |
| cholesterol | float |
| bmi | float |
| heart_rate | float |
| oxygen_level | float |
| symptoms | string |
| doctor_notes | string |

---

# Included Models

- Ensemble Model
- TF-IDF Vectorizer
- Label Encoder

---

# Logging

The project supports centralized logging for:

- API Requests
- Prediction Requests
- Errors
- Model Loading
- Inference

---

# Future Enhancements

- Explainable AI (SHAP/LIME)
- Docker Support
- Kubernetes Deployment
- Authentication
- Role-Based Access
- Batch Prediction
- Model Registry
- CI/CD Pipeline
- Cloud Deployment
- Monitoring Dashboard

---

# License

This project is intended for educational, research, and demonstration purposes.

---

# Author

Disease Prediction System

Built using

- FastAPI
- React TypeScript
- Streamlit
- Scikit-learn
- MLflow
- Python