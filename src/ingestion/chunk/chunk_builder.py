from pathlib import Path
from .models import Chunk


class ChunkBuilder:

    def build(self, path: Path, repo: str, chunks: list[str]) -> list[Chunk]:

        results: list[Chunk] = []

        for chunk in chunks:

            results.append(
                Chunk(
                    text=chunk,
                    file_path=str(path),
                    repo=repo,
                    language=path.suffix.replace(".", "")
                )
            )

        return results