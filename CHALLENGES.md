# Challenges Faced

## 1 SMTP Email Configuration
Issue:
smtp_default missing.

Resolution:
Configured Airflow SMTP connection.

---

## 2 WSL Crash / Airflow Downtime
Issue:
WSL service crashed.

Resolution:
Restarted WSL and Airflow standalone.

---

## 3 Experiment Reproducibility
Issue:
Tracking model artifacts.

Resolution:
Used DVC + MLflow.

---

## 4 Multi-service Deployment
Issue:
Separating UI and API services.

Resolution:
Docker compose architecture.

---

## 5 Monitoring Integration
Issue:
Exporting metrics.

Resolution:
Prometheus instrumentation + Grafana.
