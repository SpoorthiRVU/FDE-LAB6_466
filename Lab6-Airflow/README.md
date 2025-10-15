# Lab 6 – Apache Airflow Setup with Docker

## Objective
Install and run Apache Airflow using Docker and PostgreSQL. Execute ETL workflows with DAGs.

## Steps to Run
1. Build Docker image:
   docker build -t airflowsqlserver -f Dockerfile --no-cache .
2. Start containers:
   docker-compose up
3. Access Airflow UI at: http://localhost:9099/home
4. Trigger the DAG `etl_pipeline_postgres` from the UI.

## SQL Setup
1. Connect to PostgreSQL container:
   docker exec -it <postgres-container-name> psql -U airflow -d airflow
2. Run SQL script:
   \i /path/to/create_etl_staging.sql

## DAG
* `etl_pipeline_postgres` simulates ETL workflow: Extract → Transform → Load.
