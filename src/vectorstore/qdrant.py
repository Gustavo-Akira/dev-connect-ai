

from vectorstore.model import VectorRecord
from vectorstore.store import VectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams
from app.config import QDRANT_HOST, QDRANT_PORT, QDRANT_COLLECTION_NAME, EMBEDDING_MODEL

class QdrantVectorStore(VectorStore):
    def __init__(self) -> None:
        self.collection_name = QDRANT_COLLECTION_NAME
        self.client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
        self.ensure_collection()
        
    def ensure_collection(self) -> None:
        collections = self.client.get_collections().collections
        names = [collection.name for collection in collections]
        if self.collection_name not in names:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE)
            )

    def insert(
        self,
        records: list[VectorRecord]
    ) -> None:
        points: list[PointStruct] = []
        for record in records:
            point = PointStruct(id=record.id, vector=record.vector, payload=record.metadata)
            points.append(point)
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )    