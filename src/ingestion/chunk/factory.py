
from pathlib import Path

from ingestion.chunk.base import Chunker
from ingestion.chunk.go import GoChunker
from ingestion.chunk.java import JavaChunker
from ingestion.chunk.markdown import MarkDowmnChunker
from ingestion.chunk.react import ReactChunker


class ChunkerFactory:
    def __init__(self):
        self.chunkers: list[Chunker] = [
            JavaChunker(),
            GoChunker(),
            MarkDowmnChunker(),
            ReactChunker(),
        ]
        
    def get_chunker(self, path: Path) -> Chunker:
        for chunker in self.chunkers:
            if chunker.supports(path):
                return chunker
        return None
    