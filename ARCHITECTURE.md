# Architecture Overview — FlowCast

System Layers:

User
↓
Streamlit Frontend
↓ REST
FastAPI Backend
↓
Trained Model

Data Pipeline:
Raw Data
↓
Feature Engineering
↓
Model Training
↓
Validation

Orchestration:
Airflow DAG

Experiment Tracking:
MLflow

Versioning:
Git + DVC

Monitoring:
Prometheus
↓
Grafana

Deployment:
Docker Compose

Architecture Diagram:
See flowcastdiagram.drawio
