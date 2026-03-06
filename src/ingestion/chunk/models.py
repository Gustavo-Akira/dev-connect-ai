from dataclasses import dataclass

@dataclass
class Chunk:
    text: str
    file_path: str
    repo: str
    language: str