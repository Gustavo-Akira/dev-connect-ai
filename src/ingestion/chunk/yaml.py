from pathlib import Path
from .base import Chunker


class YAMLChunker(Chunker):

    def supports(self, path: Path) -> bool:
        return path.suffix.lower() in {".yml", ".yaml"}

    def chunk(self, path: Path, content: str) -> list[str]:

        chunks: list[str] = []

        sections = content.split("\n\n")

        for section in sections:
            section = section.strip()

            if section:
                chunks.append(section)

        return chunks