# High Level Design — FlowCast

## System Overview

FlowCast is an end-to-end MLOps system for traffic prediction composed of:

1. Data Engineering Layer
- CSV ingestion
- Feature engineering
- DVC controlled preprocessing pipeline
- Airflow orchestration DAG

2. Model Development Layer
- XGBoost training
- LightGBM benchmarking
- MLflow experiment tracking
- Model registry artifacts

3. Serving Layer
- FastAPI inference backend
- REST endpoints
- Prometheus instrumentation

4. Frontend Layer
- Streamlit UI
- REST communication with backend
- Loose coupling via APIs

5. Deployment Layer
- Dockerized frontend/backend
- Docker Compose multi-service orchestration

6. Monitoring Layer
- Prometheus metrics
- Grafana dashboards
- Health and readiness probes


## Architectural Design Principles
- Loose coupling
- Modular components
- Containerized deployment
- Reproducible ML pipelines
- Observable services
- Version-controlled data and models


## Major Interfaces
Frontend -> FastAPI REST API  
FastAPI -> Model Artifact  
Prometheus -> Metrics endpoint  
Grafana -> Prometheus datasource  
Airflow -> Pipeline orchestration  
DVC -> Pipeline dependency graph


## Throughput
Inference latency:
~150 ms

Container startup:
~5 sec

Pipeline execution:
Batch preprocessing + model training reproducible


## Technology Stack
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
