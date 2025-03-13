from cosmos import ProfileConfig
from cosmos.profiles.bigquery import GoogleCloudServiceAccountFileProfileMapping

airflow_db = ProfileConfig(
    profile_name="projeto_um",
    target_name="dev",
    profile_mapping=GoogleCloudServiceAccountFileProfileMapping(
        conn_id="my_google_cloud_platform_connection",
        profile_args={
            "project": "athena-421420",
            "dataset": "dbt_dw",
            "keyfile": "/usr/local/airflow/dags/dbt/projeto_um/athena-421420-766e358f4b1e.json",
        }
    ),
)
