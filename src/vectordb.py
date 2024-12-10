from langchain_google_community import BigQueryVectorStore
from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY


class VectorDB:
    def __init__(self, model_name, project_id, dataset_name, table_name, location):
        self.vector_db = BigQueryVectorStore(
            embedding=OpenAIEmbeddings(model=model_name, api_key=OPENAI_API_KEY),
            project_id=project_id,
            dataset_name=dataset_name,
            table_name=table_name,
            location=location,
            distance_type='COSINE'
        )


    def add_texts(self, texts, metadatas=None):
        return self.vector_db.add_texts(texts, metadatas)


    def similarity_search(self, query, k=5):
        return self.vector_db.similarity_search(query, k)