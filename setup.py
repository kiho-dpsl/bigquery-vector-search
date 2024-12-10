from src.fetcher import fetch_data
from src.preprocessor import preprocess_data
from vectordb import VectorDB
from config import(
    MODEL_NAME,
    PROJECT_ID,
    DATASET_NAME,
    TABLE_NAME,
    VECTOR_TABLE_NAME,
    LOCATION
)


def build_vectordb():
    df = fetch_data(PROJECT_ID, DATASET_NAME, TABLE_NAME)
    df = preprocess_data(df)
    texts, metadatas = df['texts'].to_list(), df['metadatas'].to_list()
    vector_db = VectorDB(MODEL_NAME, PROJECT_ID, DATASET_NAME, VECTOR_TABLE_NAME, LOCATION)
    vector_db.add_texts(texts, metadatas)
    print("VectorDB has been built successfully!")


if __name__ == "__main__":
    build_vectordb()