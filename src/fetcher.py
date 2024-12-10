from google.oauth2 import service_account
import pandas_gbq


def fetch_data(project_id, dataset_name, table_name):
    query = f"""
    SELECT *
    FROM `{project_id}.{dataset_name}.{table_name}`
    """
    print("Loading data...")
    df = pandas_gbq.read_gbq(query, project_id=project_id)
    return df