from dataclasses import dataclass


@dataclass
class QueryResponse:
    sources: list[str]
    response: str
    completion_tokens: int = 0
    prompt_tokens: int = 0