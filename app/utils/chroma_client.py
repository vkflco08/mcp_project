import chromadb

# chroma_db 폴더는 docker volume으로 유지 가능
chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection("tasks")