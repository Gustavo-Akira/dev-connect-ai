from dataclasses import dataclass

@dataclass
class VectorRecord:
    id: str
    vector: list[float]
    metadata: dict
    
@dataclass
class SearchResult:
    id: str
    metadata: dict
    text: str
    score: float