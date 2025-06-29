from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'aseem',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'flight_etl_dag',
    default_args=default_args,
    description='Flight price tracking ETL DAG',
    schedule_interval='0 8 * * *',  # every day at 8 AM
    start_date=datetime(2025, 6, 29),
    catchup=False,
    tags=['flight', 'etl'],
) as dag:

    run_etl_task = BashOperator(
        task_id='run_flight_etl',
        bash_command=(
            'echo "=== START TASK ==="; '
            '/Users/aseemshaikh/Documents/Skills/ETL/Projects/flight_tracker/fvenv/bin/python '
            '/Users/aseemshaikh/Documents/Skills/ETL/Projects/flight_tracker/main.py; '
            'echo "=== END TASK ==="'
        ),
        env={
            'GOOGLE_EMAIL': Variable.get("GOOGLE_EMAIL"),
            'GMAIL_PASSWORD': Variable.get("GMAIL_PASSWORD")
        }
    )

