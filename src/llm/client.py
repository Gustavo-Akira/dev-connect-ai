from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def generate_response(self, query: str, context: str) -> str:
        """Generates a response based on the query and context."""
        pass