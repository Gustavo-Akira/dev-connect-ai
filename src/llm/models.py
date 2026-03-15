from dataclasses import dataclass

@dataclass
class QueryResult:
    response: str
    prompt_tokens: int
    completion_tokens: int