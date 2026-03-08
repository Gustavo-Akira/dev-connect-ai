from abc import ABC, abstractmethod
from .model import SearchResult, VectorRecord


class VectorStore(ABC):

    @abstractmethod
    def insert(
        self,
        record: VectorRecord
    ) -> None:
        pass
    
    @abstractmethod
    def search(
        self,
        query_vector: list[float],
        top_k: int = 5
    ) -> list[SearchResult]:
        pass