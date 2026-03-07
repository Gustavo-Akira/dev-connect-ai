

from vectorstore.model import VectorRecord
from vectorstore.store import VectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from src.app.config import QDRANT_HOST, QDRANT_PORT, QDRANT_COLLECTION_NAME, EMBEDDING_MODEL

class QdrantVectorStore(VectorStore):
    def __init__(self) -> None:
        self.collection_name = QDRANT_COLLECTION_NAME
        self.client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

    def insert(
        self,
        records: list[VectorRecord]
    ) -> None:
        points: list[PointStruct] = []
        for record in records:
            point = PointStruct(id=record.id, vector=record.vector, payload=record.payload)
            points.append(point)
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )    