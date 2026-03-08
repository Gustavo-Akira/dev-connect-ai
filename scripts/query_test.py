from pathlib import Path
import sys
import traceback

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from vectorstore.store import VectorStore
from vectorstore.qdrant import QdrantVectorStore
from embeddings.service import EmbeddingService
import time


def main():
    start_time = time.time()
    embedding_service = EmbeddingService()
    query = "Where is the Password Recovery ?"
    query_vector = embedding_service.embed_batch([query])
    try:
        store: VectorStore = QdrantVectorStore()
    
        results = store.search(query_vector=query_vector[0], top_k=5)
        for result in results:
            print(result.metadata)
            print(result.text)
            print(result.score)
            print("------")
    except Exception as e:
        print(f"Error occurred while searching: {e}")
        traceback.print_exc()        
    total_time = time.time() - start_time
    print(f"Search completed in {total_time:.2f} seconds")


if __name__ == "__main__":
    main()