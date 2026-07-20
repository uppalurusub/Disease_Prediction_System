# 🩺 Disease Prediction System - React TypeScript Frontend

![React](https://img.shields.io/badge/React-19-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue)
![Vite](https://img.shields.io/badge/Vite-Latest-purple)
![Axios](https://img.shields.io/badge/Axios-HTTP-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview

The Disease Prediction System is a modern React TypeScript application that allows healthcare professionals to enter patient clinical information and obtain AI-powered disease predictions from a FastAPI backend.

The application follows a clean layered architecture consisting of:

- Presentation Layer
- Components
- Hooks
- Services
- API Layer
- Models

This separation makes the application scalable, reusable, and easy to maintain.

---

# Features

- React + TypeScript
- Modern Component Architecture
- Custom React Hooks
- Axios API Integration
- Strongly Typed Models
- Disease Prediction Form
- Confidence Score Visualization
- Clinical Recommendation Display
- Responsive UI
- Modular Folder Structure
- Easy FastAPI Integration

---

# Project Structure

```
src
│
├── api
│   ├── axios.ts
│   └── predictionApi.ts
│
├── components
│   └── prediction
│       ├── PredictionForm.tsx
│       └── PredictionResult.tsx
│
├── hooks
│   └── usePrediction.ts
│
├── models
│   ├── PredictionRequest.ts
│   └── PredictionResponse.ts
│
├── pages
│   └── PredictionPage.tsx
│
├── services
│   └── predictionService.ts
│
├── styles
│   └── PredictionResponse.css
│
├── App.tsx
├── main.tsx
└── index.css
```

---

# Application Architecture

```
                User
                  │
                  ▼
      PredictionForm Component
                  │
                  ▼
          usePrediction Hook
                  │
                  ▼
       predictionService.ts
                  │
                  ▼
         predictionApi.ts
                  │
                  ▼
             Axios Client
                  │
                  ▼
      FastAPI Backend (/predict)
                  │
                  ▼
       Disease Prediction Model
                  │
                  ▼
      PredictionResult Component
```

---

# Technology Stack

| Technology | Purpose |
|------------|----------|
| React | UI Framework |
| TypeScript | Strong Typing |
| Vite | Build Tool |
| Axios | HTTP Client |
| CSS | Styling |
| FastAPI | Backend API |
| REST API | Communication |

---

# Functional Modules

## 1. Patient Information Form

Collects:

- Age
- Blood Pressure
- Glucose
- Cholesterol
- BMI
- Heart Rate
- Oxygen Level
- Symptoms
- Doctor Notes

---

## 2. Disease Prediction

Sends patient information to

```
POST /predict/
```

Backend returns

```json
{
    "prediction": "Heart Disease",
    "confidence": 0.94
}
```

---

## 3. Prediction Results

Displays

- Predicted Disease
- Confidence Percentage
- Progress Bar
- Clinical Recommendation

Example

```
Disease:
Heart Disease

Confidence:
94%

Recommendation:
Immediate specialist consultation recommended.
```

---

# Folder Responsibilities

## api/

Contains all HTTP communication.

```
axios.ts
```

Creates reusable Axios client.

```
predictionApi.ts
```

Calls backend prediction endpoint.

---

## components/

Contains reusable UI components.

### PredictionForm

Responsible for

- Form Rendering
- Validation
- Collecting Input

### PredictionResult

Responsible for

- Prediction Display
- Confidence Progress Bar
- Recommendation

---

## hooks/

Contains business logic.

### usePrediction

Responsible for

- Loading State
- Calling Services
- Managing API Response

---

## models/

Contains TypeScript interfaces.

### PredictionRequest

```typescript
{
  age
  bp
  glucose
  cholesterol
  bmi
  heart_rate
  oxygen_level
  symptoms
  doctor_notes
}
```

### PredictionResponse

```typescript
{
   prediction
   confidence
}
```

---

## services/

Acts as business layer.

```
Prediction Service
```

Separates UI from API implementation.

---

# API Configuration

Base URL

```
http://127.0.0.1:8000
```

Configured in

```
src/api/axios.ts
```

---

# API Endpoint

## Predict Disease

```
POST /predict/
```

### Request

```json
{
  "age": 52,
  "bp": 145,
  "glucose": 180,
  "cholesterol": 240,
  "bmi": 31.5,
  "heart_rate": 92,
  "oxygen_level": 96,
  "symptoms": "chest pain fatigue dizziness",
  "doctor_notes": "Patient reports chest pain and fatigue"
}
```

### Response

```json
{
    "prediction": "Heart Disease",
    "confidence": 0.94
}
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-repository/disease-prediction-ui.git
```

---

## Navigate

```bash
cd disease-prediction-ui
```

---

## Install Dependencies

```bash
npm install
```

---

## Start Development Server

```bash
npm run dev
```

---

Application runs at

```
http://localhost:5173
```

---

# Build Production

```bash
npm run build
```

---

# Preview Production Build

```bash
npm run preview
```

---

# Development Workflow

```
User Input
      │
      ▼
Prediction Form
      │
      ▼
Validation
      │
      ▼
API Request
      │
      ▼
FastAPI Backend
      │
      ▼
Prediction Response
      │
      ▼
Result Visualization
```

---

# Current Features

- Typed API Integration
- Disease Prediction Form
- Confidence Indicator
- Clinical Recommendation
- Responsive Layout
- Clean Architecture
- Modular Components
- Reusable Services
- Custom Hooks

---

# Future Enhancements

- Authentication
- Dashboard
- Prediction History
- PDF Report Export
- Patient Management
- Charts and Analytics
- Risk Gauge Visualization
- Dark Mode
- Form Validation with React Hook Form
- Toast Notifications
- Environment Variable Support
- Unit Testing
- Docker Support
- CI/CD Pipeline

---

# Coding Standards

- Functional Components
- TypeScript Interfaces
- Custom Hooks
- Separation of Concerns
- Modular Architecture
- Strong Typing
- Reusable Services

---

# Recommended Improvements

- Add React Router for multi-page navigation.
- Use environment variables (`VITE_API_BASE_URL`) instead of hardcoded API URLs.
- Add centralized error handling with user-friendly notifications.
- Introduce React Query or TanStack Query for API state management.
- Use React Hook Form with Zod for robust form validation.
- Implement loading skeletons and error boundaries.
- Add authentication and protected routes if required.
- Write unit tests using Vitest and React Testing Library.
- Configure ESLint, Prettier, and Husky for code quality.
- Containerize the application using Docker.

---

# License

This project is licensed under the MIT License.

---

# Author

**Disease Prediction System**

Built with

- React
- TypeScript
- Axios
- FastAPI
- REST APIs
- Modern Frontend Architecture