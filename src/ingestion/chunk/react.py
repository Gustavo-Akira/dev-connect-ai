import re
from pathlib import Path
from typing import Iterable
from .base import Chunker


class ReactChunker(Chunker):

    COMPONENT_PATTERN = re.compile(
        r"(export\s+(default\s+)?(function|const)\s+\w+)"
    )

    def supports(self, file_path: Path) -> bool:
        return file_path.suffix.lower() in {".tsx", ".jsx", ".ts", ".js"}

    def chunk(self, file_path: Path, content: str) -> Iterable[str]:

        matches = list(self.COMPONENT_PATTERN.finditer(content))

        if not matches:
            yield content
            return

        for i, match in enumerate(matches):
            start = match.start()

            if i + 1 < len(matches):
                end = matches[i + 1].start()
            else:
                end = len(content)

            yield content[start:end].strip()
        