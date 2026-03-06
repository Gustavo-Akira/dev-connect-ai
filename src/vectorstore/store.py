from abc import ABC, abstractmethod
from .model import VectorRecord


class VectorStore(ABC):

    @abstractmethod
    def insert(
        self,
        record: VectorRecord
    ) -> None:
        pass