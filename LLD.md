# Low Level Design (LLD) — FlowCast Traffic Predictor

# 1. Overview
FlowCast consists of two loosely coupled software components:

1. Frontend UI (Streamlit)
2. Backend Inference API (FastAPI)

Communication occurs only through REST APIs over HTTP.

---

# 2. Component Design

## 2.1 Frontend Component
Technology:
- Streamlit

Responsibilities:
- Collect user inputs
- Send prediction requests
- Display traffic prediction
- Visualize MLOps pipeline

Input fields:
- temp
- rain_1h
- snow_1h
- clouds_all
- hour
- day_of_week
- month
- day
- weather_main

Output:
- Predicted traffic volume
- Traffic category:
  - Low
  - Moderate
  - Heavy

---

## 2.2 Backend Component
Technology:
- FastAPI

Responsibilities:
- Validate request payload
- Generate engineered features
- Run model inference
- Return prediction
- Expose monitoring endpoints

Model:
- XGBoost Regressor
Serialized artifact:
- model.ubj

---

# 3. API Endpoint Specification

## 3.1 Health Endpoint

Endpoint:
GET /health

Request:
None

Response:
{
 "status":"healthy",
 "model_loaded":true
}

HTTP:
200 OK

Purpose:
Container health probe

---

## 3.2 Readiness Endpoint

Endpoint:
GET /ready

Response:
{
 "status":"ready"
}

Purpose:
Readiness probe

---

## 3.3 Metrics Endpoint

Endpoint:
GET /metrics

Purpose:
Prometheus instrumentation metrics

Output:
Prometheus metric stream

---

## 3.4 Prediction Endpoint

Endpoint:
POST /predict

Request Schema:

{
 "temp":290,
 "rain_1h":0,
 "snow_1h":0,
 "clouds_all":75,
 "hour":8,
 "day_of_week":2,
 "month":10,
 "day":3,
 "weather_main":"Clouds"
}

Processing Steps:
1 Validate payload
2 Feature engineering:
- cyclical encoding
- lag features
- rolling statistics
- one-hot encoding

3 Model inference

Response:

{
 "predicted_traffic_volume":4832
}

HTTP:
200 OK

---

# 4. Error Handling

Invalid Input:
400 Bad Request

Inference Failure:
500 Internal Server Error

Example:

{
 "detail":"Inference failed"
}

Handled via:
- FastAPI exceptions
- Logging
- Validation checks

---

# 5. Feature Engineering Logic

Derived Features:

Temporal:
- hour_sin
- hour_cos
- dow_sin
- dow_cos
- month_sin
- month_cos

Behavioral:
- is_weekend
- is_rush_hour

Lag Features:
- lag_1
- lag_24
- lag_168

Rolling:
- rolling_mean_6
- rolling_std_6
- rolling_mean_24
- rolling_std_24

Categorical:
- weather one-hot features
- holiday one-hot features

---

# 6. Request Flow

User Input
↓
Streamlit UI
↓
POST /predict
↓
FastAPI
↓
Feature Engineering
↓
XGBoost Model
↓
Prediction Response
↓
UI Output

---

# 7. Container Architecture

docker-compose services:

frontend
- port 8501

api
- port 8001

Communication:
frontend -> api via REST

Loose coupling maintained.

---

# 8. Logging Design

Logs captured:
- incoming requests
- prediction success
- inference errors

Purpose:
- debugging
- monitoring
- audit trail

---

# 9. Security / Validation

Implemented:
- Pydantic schema validation
- typed request models
- controlled API interface

---

# 10. Acceptance Criteria

System accepted if:

- Prediction API responds successfully
- Frontend consumes API correctly
- Containers start successfully
- Monitoring endpoints accessible
- Prediction latency <200ms

---

# 11. Future Extensions

- Drift detection service
- Retraining pipeline
- CI/CD integration
- Model registry promotion workflow