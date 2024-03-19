import datetime as dt
from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from etl import etl_process

default_args = {
    'owner': 'Pedro',
    'depends_on_past': False,
    'start_date': '2024-03-18',
    'email': ['email@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('dag_elt_weather',
          default_args = default_args,
          description = 'Pipeline ETL using Weather API',
          schedule_interval = timedelta(minutes=60)
)

execute_etl = PythonOperator(task_id = 'etl_python_script',
                             python_callable = etl_process,
                             dag = dag
)

execute_etl