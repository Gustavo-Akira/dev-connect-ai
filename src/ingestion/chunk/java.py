
import re

from base import BaseChunker
from pathlib import Path


class JavaChunker(BaseChunker):
    def chunk(self, path: Path, content: str) -> list[str]:
        chunks = []
        class_patterns = re.compile(r'\bclass\s+(\w+)')
        for match in class_patterns.finditer(content):
            start_index = match.start()
            brace_count = 0
            inside_class = False
            for i in range(start_index, len(content)):
                if content[i] == '{':
                    brace_count += 1
                    inside_class = True
                elif content[i] == '}':
                    brace_count -= 1
                    if inside_class and brace_count == 0:
                        chunks.append(content[start_index:i + 1])
                        break
        return chunks
    def supports(self, path: Path) -> bool:
        return path.suffix.lower() == '.java'