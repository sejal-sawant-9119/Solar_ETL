from airflow import DAG
from airflow .operators.python import PythonOperator
from datetime import datetime

def say_hello():
	print("Hello Sejal! Your Airflow is working.")

with DAG(
	dag_id = "hello_world_dag",
	start_date = datetime(2025,7,15),
	schedule_interval = "@daily",
	catchup = False
) as dag:
	task = PythonOperator(
		task_id = "say_hello_task",
		python_callable = say_hello
	)