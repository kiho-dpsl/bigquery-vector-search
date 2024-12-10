import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__name__).absolute().parent
load_dotenv(BASE_DIR / ".env")

GOOGLE_API_CREDENTIALS = BASE_DIR / "auth" / "google_api_credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(GOOGLE_API_CREDENTIALS)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_NAME="text-embedding-3-small"
PROJECT_ID = os.getenv('PROJECT_ID')
DATASET_NAME = "600_kiho"
TABLE_NAME = "sample_data"
VECTOR_TABLE_NAME = "vector_db"
LOCATION = "asia-northeast1"