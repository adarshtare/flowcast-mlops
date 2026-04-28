# Airflow Orchestration Pipeline

DAG Name:
flowcast_ml_pipeline

Pipeline Stages:
1. Data Ingestion
2. Feature Engineering
3. Model Training
4. Model Validation
5. Deployment Ready

Execution Order:
data_ingestion
   ->
feature_engineering
   ->
model_training
   ->
model_validation
   ->
deployment_ready

Airflow is used as orchestration layer for automated scheduled retraining.

Schedule:
@daily

Purpose:
- Automated retraining
- Pipeline orchestration
- Failure tracking
- Production readiness
