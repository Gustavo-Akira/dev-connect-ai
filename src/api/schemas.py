from dataclasses import dataclass

from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str
    
class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    completion_tokens: int = 0
    prompt_tokens: int = 0