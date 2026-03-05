
from pathlib import Path

from ingestion.chunk.base import Chunker


class MarkDowmnChunker(Chunker):
    def supports(self, path):
        return path.suffix.lower() in ['.md', '.markdown']
            
    def chunk(self, path: Path, content: str) -> list[str]:
        sections = content.split("\n## ")
        return [section.strip() for section in sections if section.strip()]
               
    