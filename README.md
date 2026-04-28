# 🚦 FlowCast — Traffic Forecasting MLOps Platform

## 🧩 Overview
FlowCast is an end-to-end MLOps application for intelligent traffic forecasting that combines
machine learning, pipeline orchestration, experiment tracking, monitoring and containerized deployment.

The project implements a full AI product lifecycle:
- Data ingestion pipeline
- Feature engineering
- Model training and validation
- FastAPI model serving
- Experiment tracking using MLflow
- Workflow orchestration using Airflow
- Data & model versioning using DVC
- Monitoring with Prometheus + Grafana
- Dockerized deployment using Docker Compose

---

# 📂 Repository Structure

```bash
flowcast/
├── airflow_dags/
├── src/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── tests/

├── Dockerfile.api
├── Dockerfile.ui
├── docker-compose.yml
├── dvc.yaml
├── dvc.lock
├── MLproject
├── prometheus.yml
├── conda.yaml

├── README.md
├── ARCHITECTURE.md
├── AIRFLOW_PIPELINE.md
├── GRAFANA_MONITORING.md
├── HLD.md
├── LLD.md
├── CI_CD.md
├── CHALLENGES.md
├── TEST_PLAN.md
├── TEST_REPORT.md
├── USER_MANUAL.md
├── report_flowcast.pdf

├── flowcastdiagram.drawio
└── requirements.txt
```

---

# 🎯 Project Goals
- Build scalable traffic forecasting system
- Implement full MLOps pipeline locally (no cloud)
- Enable reproducible experiments
- Serve predictions through APIs
- Monitor model/system behavior in near real time
- Demonstrate CI/CD and production-style deployment

---

# ⚙️ Tech Stack

## Machine Learning
- Python
- Scikit-learn
- XGBoost
- MLflow

## MLOps
- Apache Airflow
- DVC
- Docker + Docker Compose
- Prometheus
- Grafana

## Backend / Serving
- FastAPI
- REST APIs

---

# 🔄 End-to-End Pipeline

## Airflow Pipeline
Implemented DAG:

```text
Data Ingestion
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Validation
   ↓
Deployment Ready
   ↓
Email Notification
```

Airflow handles:
- Scheduling
- Task dependency management
- Pipeline tracking
- Failure alerts
- Success notifications

---

# 🧪 MLflow Experiment Tracking
Tracked:
- Hyperparameters
- RMSE / model metrics
- Artifacts
- Model versions
- Training runs

Airflow triggers model training stage which logs directly into MLflow.

Integration:

```text
Airflow → train.py → MLflow Tracking Server
```

---

# 📦 Data Versioning with DVC

DVC manages:
- Dataset versioning
- Pipeline stages
- Reproducibility

Pipeline stages:
- ingest
- features
- train

Run:

```bash
dvc repro
dvc dag
```

---

# 🌐 FastAPI Inference APIs

Endpoints:

## Health
```http
GET /health
```

## Readiness
```http
GET /ready
```

## Prediction
```http
POST /predict
```

Input:
```json
{
 "traffic_volume": 1200,
 "weather": "rain"
}
```

Output:
```json
{
 "prediction": 1347
}
```

---

# 📊 Monitoring & Instrumentation

Implemented with:

- Prometheus metrics exporter
- Grafana dashboards

Monitored:
- API latency
- Request counts
- Model inference metrics
- Error rates
- Pipeline execution status

Alerting supported for:
- Failure spikes
- Drift signals
- High latency

---

# 🐳 Dockerized Deployment

Separate services:
- Frontend container
- Backend container
- Monitoring services

Run:

```bash
docker-compose up --build
```

---

# 🧠 Features
✅ Traffic forecasting model  
✅ Pipeline orchestration  
✅ Experiment tracking  
✅ Monitoring dashboards  
✅ Docker deployment  
✅ DVC reproducibility  
✅ REST model serving  
✅ Email alerts

---

# 🧪 Testing
Includes:
- Unit tests
- API tests
- Pipeline tests

Acceptance criteria:
- Successful DAG completion
- Prediction latency < 200ms
- All API tests pass

See:
- TEST_PLAN.md
- TEST_REPORT.md

---

# 📈 MLOps Components Implemented

| Component | Tool |
|---------|------|
| Data Engineering | Airflow |
| Version Control | Git + DVC |
| Experiment Tracking | MLflow |
| Model Serving | FastAPI |
| Monitoring | Prometheus/Grafana |
| Containerization | Docker |
| CI Pipeline | GitHub Actions |

---

# 🚀 Running Project

## Install
```bash
pip install -r requirements.txt
```

## Start Airflow
```bash
airflow standalone
```

## Start API
```bash
uvicorn app:app --reload
```

## Start Full Stack
```bash
docker-compose up
```

---

# 📷 Visualizations
Included:
- Airflow DAG UI
- MLflow tracking UI
- Grafana dashboards
- DVC DAG
- Architecture diagrams

See documentation files.

---

# 🏆 Highlights
- Full end-to-end MLOps implementation
- Local reproducible deployment
- Production-style monitoring
- Loose coupling via REST APIs
- Orchestrated ML pipeline

---

# 🔮 Future Work
- Drift detection automation
- Continuous retraining
- Kubernetes deployment
- Streaming inference
- Advanced traffic deep learning models

---

## 👨‍💻 Author
Adarsh Tare

MLOps Project — FlowCast
