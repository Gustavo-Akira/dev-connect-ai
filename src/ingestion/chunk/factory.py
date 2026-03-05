
from pathlib import Path

from ingestion.chunk.base import Chunker
from ingestion.chunk.java import JavaChunker


class ChunkerFactory:
    def __init__(self):
        self.chunkers: list[Chunker] = [
            JavaChunker(),
        ]
        
    def get_chunker(self, path: Path) -> Chunker:
        for chunker in self.chunkers:
            if chunker.supports(path):
                return chunker
        return None
    