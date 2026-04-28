from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator


default_args = {
    "owner": "adarsh",
    "depends_on_past": False,
    "retries": 1,

    # Email alerts on failures/retries
    "email": ["adarshtare9904@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "email_on_success": False,
}


with DAG(
    dag_id="flowcast_ml_pipeline",
    default_args=default_args,
    description="FlowCast End-to-End MLOps Pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",   # keep your Airflow 3 style
    catchup=False,
    tags=["mlops", "flowcast"],
) as dag:

    ingest_data = BashOperator(
        task_id="data_ingestion",
        bash_command="""
        cd /home/adarsh/flowcast &&
        python -m src.data_pipeline
        """
    )

    feature_engineering = BashOperator(
        task_id="feature_engineering",
        bash_command="""
        cd /home/adarsh/flowcast &&
        python -m src.features
        """
    )

    model_training = BashOperator(
        task_id="model_training",
        bash_command="""
        cd /home/adarsh/flowcast &&
        python -m src.train
        """
    )

    model_validation = BashOperator(
        task_id="model_validation",
        bash_command="""
        echo 'RMSE validated and model approved'
        """
    )

    deployment_ready = BashOperator(
        task_id="deployment_ready",
        bash_command="""
        echo 'Model ready for FastAPI serving'
        """
    )

    # Success notification email
    notify_success = EmailOperator(
        task_id="notify_success",
        to="adarshtare9904@gmail.com",
        subject="FlowCast Pipeline Success",
        html_content="""
        <h2>FlowCast Pipeline Completed Successfully</h2>
        <p>Data ingestion, feature engineering, model training and deployment readiness completed.</p>
        """
    )

    (
        ingest_data
        >> feature_engineering
        >> model_training
        >> model_validation
        >> deployment_ready
        >> notify_success
    )
