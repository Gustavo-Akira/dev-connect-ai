from abc import ABC, abstractmethod
from pathlib import Path


class Chunker(ABC):
    @abstractmethod
    def chunk(self, path: Path, content: str) -> list[str]:
        """Chunk the file at the given path and return a list of chunks."""
        pass 
    @abstractmethod
    def supports(self, path: Path) -> bool:
        """Return True if this chunker supports the given file path."""
        pass