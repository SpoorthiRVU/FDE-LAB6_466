from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('etl_pipeline_postgres', start_date=datetime(2025,10,8), schedule_interval='@daily', catchup=False) as dag:
    extract = BashOperator(task_id='extract', bash_command='echo "Extracting data from source"')
    transform = BashOperator(task_id='transform', bash_command='echo "Transforming data"')
    load = BashOperator(task_id='load', bash_command='echo "Loading data into etl_staging schema"')
    extract >> transform >> load
