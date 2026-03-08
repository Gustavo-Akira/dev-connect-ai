from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class QueryRequest(BaseModel):
    question: str
    
@dataclass
class QueryResponse(BaseModel):
    answer: str
    sources: list[str]