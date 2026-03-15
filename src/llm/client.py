from abc import ABC, abstractmethod

from llm.models import QueryResult

class LLMClient(ABC):
    @abstractmethod
    def generate_response(self, query: str, context: str) -> QueryResult:
        """Generates a response based on the query and context."""
        pass