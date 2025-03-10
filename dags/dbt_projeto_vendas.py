from airflow.decorators import dag, task
from datetime import datetime
import subprocess

@dag(
    dag_id="dbt_projeto_vendas",
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
)
def dbt_projeto_vendas():

    @task
    def run_dbt_ls():
        # Define o comando para listar os recursos do projeto dbt
        command = "cd /usr/local/airflow/projeto_um && dbt ls -s tag:vendas --profiles-dir ."
        # Executa o comando e captura a saída
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        # Imprime a saída no log do Airflow
        print(result.stdout)
        return result.stdout

    run_dbt_ls()

dag_instance = dbt_projeto_vendas()
