import chromadb
from chromadb.config import Settings

chroma_client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"  # Docker 사용 시 볼륨으로 연결 추천
))

collection = chroma_client.get_or_create_collection("tasks")