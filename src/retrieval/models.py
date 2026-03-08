from dataclasses import dataclass


@dataclass
class QueryResponse:
    sources: list[str]
    response: str