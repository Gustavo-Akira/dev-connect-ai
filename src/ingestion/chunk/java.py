import re
from pathlib import Path
from ingestion.chunk.base import Chunker


class JavaChunker(Chunker):

    CLASS_PATTERN = re.compile(r'\b(class|interface|enum)\s+\w+')

    def chunk(self, path: Path, content: str) -> list[str]:

        chunks = []

        for match in self.CLASS_PATTERN.finditer(content):

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

                        chunk = content[start_index:i + 1].strip()

                        if chunk:
                            chunks.append(chunk)

                        break

        if not chunks:
            return [content]

        return chunks

    def supports(self, path: Path) -> bool:
        return path.suffix.lower() == '.java'