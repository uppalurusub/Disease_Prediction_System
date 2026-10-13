# Disease Prediction System — Streamlit Frontend

A modular Streamlit web application for collecting patient health indicators, sending them to a prediction API, displaying the returned disease prediction and confidence score, and downloading the response as a CSV file.

> **Important medical disclaimer:** This application is a software prototype, not a medical device or diagnostic service. Predictions are not a substitute for evaluation by a qualified healthcare professional. Do not use the output as the sole basis for diagnosis, treatment, triage, or other clinical decisions. The model, training data, validation results, and clinical suitability are not included in this repository and have not been verified.

## Contents

- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Run the Application](#run-the-application)
- [How to Use](#how-to-use)
- [Prediction API Contract](#prediction-api-contract)
- [Response and Downloads](#response-and-downloads)
- [Troubleshooting](#troubleshooting)
- [Security and Privacy](#security-and-privacy)
- [Limitations and Recommended Enhancements](#limitations-and-recommended-enhancements)
- [License](#license)

## Features

- **Patient health input form** with numeric fields for age, blood pressure, glucose, cholesterol, BMI, heart rate, and oxygen level.
- **Clinical context fields** for symptoms and doctor notes.
- **API integration** using an HTTP `POST` request to a configurable prediction endpoint.
- **Prediction result display** showing the predicted disease label and confidence score.
- **Confidence visualization** using a Streamlit progress bar and a percentage metric.
- **CSV export** of the fields returned by the prediction API.
- **Modular organization** separating API calls, UI components, configuration, and formatting utilities.

## Architecture

The application is a Streamlit frontend. It does **not** contain the disease prediction model or backend API implementation.

```text
Browser
  |
  v
Streamlit UI (app.py)
  |
  v
Disease Prediction page
  |
  +--> Patient input form (components/request_form.py)
  |
  +--> API client (api/api_client.py)
  |       |
  |       v
  |   HTTP POST /predict/
  |       |
  |       v
  |   External prediction backend (not included)
  |
  +--> Result view (components/response_view.py)
          |
          +--> Prediction label
          +--> Confidence percentage / progress bar
          +--> CSV download
```

### Request flow

1. The user opens the Disease Prediction page.
2. The form collects health indicators, symptoms, and doctor notes.
3. On **Predict Disease**, the frontend sends the form values as a JSON request body.
4. The backend processes the request and returns JSON.
5. The frontend displays the prediction and confidence, or an error message if the request fails.
6. The user can download the returned response fields as `prediction.csv`.

## Project Structure

```text
disease-prediction-system-streamlit-app/
├── app.py
├── requirements.txt
├── api/
│   ├── __init__.py
│   └── api_client.py
├── components/
│   ├── __init__.py
│   ├── request_form.py
│   ├── response_view.py
│   └── sidebar.py
├── pages/
│   └── 1_Disease_Prediction.py
└── utils/
    ├── __init__.py
    ├── config.py
    └── formatters.py
```

| File | Responsibility |
|---|---|
| `app.py` | Configures the Streamlit page and displays the application landing page. |
| `pages/1_Disease_Prediction.py` | Renders the prediction page and coordinates the form, API call, and result view. |
| `components/request_form.py` | Collects patient indicators and clinical text fields. |
| `components/response_view.py` | Displays prediction output and provides CSV download. |
| `components/sidebar.py` | Renders the sidebar heading. |
| `api/api_client.py` | Sends the prediction request and handles HTTP/client exceptions. |
| `utils/config.py` | Defines the API base URL and prediction endpoint. |
| `utils/formatters.py` | Provides a helper to convert prediction results into a pandas DataFrame. |
| `requirements.txt` | Lists the Python package dependencies. |

## Prerequisites

- Python 3.10 or later is recommended.
- `pip`
- Access to a compatible prediction backend.
- The backend must be reachable from the machine running Streamlit.

The included frontend dependencies are Streamlit, Requests, and pandas. The repository does not include a backend server, model artifact, training dataset, or model evaluation report.

## Installation

### 1. Extract the project

Extract `disease-prediction-system-streamlit-app.zip` and open a terminal in the project directory:

```bash
cd disease-prediction-system-streamlit-app
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use a permitted shell or activate the environment using the command appropriate for your system.

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

The API endpoint is currently defined in `utils/config.py`:

```python
API_BASE_URL = "http://localhost:8000"
PREDICT_ENDPOINT = f"{API_BASE_URL}/predict/"
```

By default, the frontend calls:

```text
POST http://localhost:8000/predict/
```

Start your compatible backend on port `8000`, or update `API_BASE_URL` to the correct host and port. The backend must expose the expected route and accept the request fields described below.

For local development, `localhost` means the same machine or environment where the Streamlit process runs. If the backend runs in a different container or on another host, configure a reachable service hostname or address. Do not expose an unauthenticated prediction API publicly.

For deployment, consider moving this setting to an environment variable or Streamlit secrets rather than hard-coding it.

## Run the Application

From the project root, run:

```bash
streamlit run app.py
```

Streamlit will print a local URL, commonly:

```text
http://localhost:8501
```

Open that URL in a browser. Use the **Pages** navigation to open **Disease Prediction**.

The frontend and prediction backend are separate processes. Starting Streamlit alone does not start the backend or make predictions possible.

## How to Use

1. Start the prediction backend and confirm that its endpoint is reachable.
2. Start the Streamlit application.
3. Open **Disease Prediction** from the Streamlit page navigation.
4. Enter the patient's available health indicators.
5. Optionally enter symptoms and doctor notes.
6. Select **Predict Disease** and wait for the API response.
7. Review the returned prediction and confidence score with appropriate clinical caution.
8. Select **Download Prediction** to export the response fields as a CSV file.

### Input fields

| Field | UI input / current range | Default |
|---|---|---:|
| `age` | Integer, 1–120 | 52 |
| `bp` | Integer, 60–250 | 145 |
| `glucose` | Integer, 40–500 | 180 |
| `cholesterol` | Integer, 50–500 | 240 |
| `bmi` | Decimal, 10–60 | 31.5 |
| `heart_rate` | Integer, 30–220 | 92 |
| `oxygen_level` | Integer, 50–100 | 96 |
| `symptoms` | Free text | Empty |
| `doctor_notes` | Free text | Empty |

These ranges and defaults are implemented in the UI; they should not be interpreted as validated clinical ranges or recommended values. The frontend does not currently establish units for every measurement, validate clinical plausibility, or enforce required symptoms/notes.

## Prediction API Contract

The API client sends a JSON body containing the form fields. A request may look like this:

```json
{
  "age": 52,
  "bp": 145,
  "glucose": 180,
  "cholesterol": 240,
  "bmi": 31.5,
  "heart_rate": 92,
  "oxygen_level": 96,
  "symptoms": "Fatigue and increased thirst",
  "doctor_notes": "Example note for testing only"
}
```

The backend implementation was not present in the supplied ZIP, so the exact schema and response contract cannot be confirmed from this repository.

The result component expects a JSON object with at least these fields:

```json
{
  "prediction": "Example prediction label",
  "confidence": 0.87
}
```

The `prediction` field is displayed as the predicted disease label. The `confidence` field is converted to a floating-point number and displayed as a percentage. The example values above are illustrative only and are **not** a real prediction.

The current UI treats confidence values of `0.80` or higher as success, values from `0.50` to below `0.80` as warning, and lower values as an error-style display. These are presentation thresholds only; they do not demonstrate that the model is clinically accurate or that the prediction is safe.

The backend should document its request/response schema, error format, confidence semantics, supported disease classes, model version, and intended use. In particular, confirm whether `confidence` is a calibrated probability or merely a model score before presenting it as a probability.

## Response and Downloads

The response view displays:

- The prediction label.
- The confidence percentage.
- A confidence progress bar.
- A CSV download of all top-level fields returned by the API.

The CSV is generated from the returned JSON object's top-level key/value pairs. Nested objects may not produce a useful tabular representation without additional flattening. The download may contain sensitive health information if the backend returns it; handle the file accordingly.

## Troubleshooting

### The app cannot connect to the API

- Confirm the backend is running.
- Check `API_BASE_URL` and `PREDICT_ENDPOINT` in `utils/config.py`.
- Test the endpoint from the same machine or container where Streamlit runs.
- Check backend logs, firewall rules, container networking, and port mappings.
- Confirm that the backend route is `/predict/` and accepts `POST` requests.

### The API returns an HTTP error

The client calls `raise_for_status()`, so non-success HTTP responses are returned to the UI as an error message. Review the backend response and logs for schema validation errors, missing fields, or server failures.

### The response is missing `prediction` or `confidence`

The result view falls back to `"Unknown"` for a missing prediction and `0` for a missing confidence. Confirm that the backend response matches the expected response contract.

### Confidence rendering fails

The frontend expects `confidence` to be convertible to a float and suitable for the Streamlit progress bar. Ensure it is numeric and within the range `0.0` to `1.0`; add explicit response validation before using this application beyond a prototype.

### The page is not visible

Run `streamlit run app.py` from the project root and use Streamlit's **Pages** navigation. Verify that the `pages/1_Disease_Prediction.py` file exists in the expected location.

## Security and Privacy

Patient health information is sensitive. Before using real patient data:

- Do not send identifiable patient information to an unapproved service.
- Use TLS/HTTPS for traffic outside a trusted local development environment.
- Add authentication and authorization to the API and frontend where appropriate.
- Apply least-privilege access, secret management, and network restrictions.
- Define data minimization, retention, deletion, and audit policies.
- Avoid logging symptoms, doctor notes, identifiers, or full request/response bodies unless specifically approved and protected.
- Review applicable privacy, security, and healthcare regulations for the deployment jurisdiction.
- Test for input validation, injection risks, unauthorized access, and data leakage.
- Establish clinical oversight, model validation, bias/fairness assessment, and monitoring before any real-world clinical use.

The current code does not implement authentication, role-based access control, audit logging, or a dedicated PHI-handling policy.

## Limitations and Recommended Enhancements

The supplied code is a lightweight frontend prototype. Before production use, consider:

1. **Configuration:** Read the backend URL from environment variables or Streamlit secrets.
2. **Schema validation:** Validate request and response payloads with explicit models and clear error messages.
3. **Error handling:** Distinguish connection failures, timeouts, HTTP errors, invalid JSON, and unexpected response structures.
4. **Clinical safety:** Add appropriate warnings, clinician review workflows, and clearly defined intended use.
5. **Model governance:** Document training data provenance, validation methodology, performance by subgroup, calibration, limitations, and model version.
6. **Privacy and security:** Add authentication, authorization, secure transport, audit controls, and approved data-retention policies.
7. **Testing:** Add unit tests for UI helpers and API client behavior, plus integration tests against a test backend.
8. **Accessibility and UX:** Clarify units, required fields, allowed ranges, and validation feedback.
9. **Observability:** Add privacy-safe operational metrics and structured error reporting.
10. **Deployment:** Add pinned dependency versions, a deployment guide, health checks, and container configuration if required.

## License

No license file was included in the supplied project archive. Add an appropriate `LICENSE` file before redistributing or publishing the project. Until a license is specified, do not assume that the code is licensed for unrestricted reuse.
