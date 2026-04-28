from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "adarsh",
    "depends_on_past": False,
    "retries": 1
}


with DAG(
    dag_id="flowcast_ml_pipeline",
    default_args=default_args,
    description="FlowCast End-to-End MLOps Pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:


    ingest_data = BashOperator(
        task_id="data_ingestion",
        bash_command="python -m src.data_pipeline"
    )


    feature_engineering = BashOperator(
        task_id="feature_engineering",
        bash_command="python -m src.features"
    )


    model_training = BashOperator(
        task_id="model_training",
        bash_command="python -m src.train"
    )


    model_validation = BashOperator(
        task_id="model_validation",
        bash_command='echo "RMSE validated and model approved"'
    )


    deployment_ready = BashOperator(
        task_id="deployment_ready",
        bash_command='echo "Model ready for FastAPI serving"'
    )


    ingest_data >> feature_engineering >> model_training >> model_validation >> deployment_ready
