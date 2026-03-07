from dataclasses import dataclass

@dataclass
class VectorRecord:
    id: str
    vector: list[float]
    metadata: dict