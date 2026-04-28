# High Level Design — FlowCast

# 1. Problem Statement
Build an end-to-end MLOps platform for traffic prediction supporting:

- scalable model training
- reproducible pipelines
- monitoring
- API deployment
- containerized serving

---

# 2. System Overview

FlowCast consists of:

## Data Engineering Layer
- CSV ingestion
- Feature engineering
- DVC controlled preprocessing
- Airflow orchestration DAG

## Model Development Layer
- XGBoost training
- LightGBM benchmarking
- MLflow experiment tracking
- Model registry

## Serving Layer
- FastAPI inference backend
- REST APIs
- Prometheus instrumentation

## Frontend Layer
- Streamlit UI
- REST communication
- Loose coupling

## Deployment Layer
- Dockerized frontend/backend
- Docker Compose orchestration

## Monitoring Layer
- Prometheus metrics
- Grafana dashboards
- Health probes

---

# 3. Architecture Principles

- Loose coupling
- Modular architecture
- Reproducibility
- Observability
- Containerization
- Version control for data/models

---

# 4. Design Choice Rationale

## Why Airflow?
Used for:
- scheduling
- orchestration
- dependency tracking

Preferred over cron for DAG support.

## Why MLflow?
Used for:
- experiment tracking
- metrics logging
- model registry

## Why DVC?
Provides:
- data versioning
- reproducibility
- CI style ML pipelines

## Why FastAPI?
Chosen for:
- lightweight serving
- REST APIs
- high performance

---

# 5. Major Interfaces

Frontend → FastAPI  
FastAPI → Model Artifact  
Airflow → ML pipeline orchestration  
Airflow Training Task → MLflow  
DVC → Pipeline DAG  
Prometheus → Metrics endpoint  
Grafana → Monitoring dashboards

---

# 6. System Throughput

Inference latency:
~150 ms

Container startup:
~5 sec

Pipeline throughput:
Batch preprocessing + model training reproducible.

---

# 7. Deployment Architecture

Dockerized services:
- frontend
- backend
- monitoring

Managed using docker-compose.

Loose coupling preserved through REST APIs.

---

# 8. Technology Stack

Git  
DVC  
Airflow  
MLflow  
FastAPI  
Prometheus  
Grafana  
Docker  
Streamlit  
XGBoost

---

# 9. Future Scalability

Future extensions:
- retraining automation
- drift detection
- kubernetes deployment
- streaming inference
