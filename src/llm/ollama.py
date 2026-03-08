import requests
from .client import LLMClient

class OllamaClient(LLMClient):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.base_url = "http://localhost:11434"

    def query(self, query: str,context: str) -> str:
        prompt = """
            You are an assistant helping developers understand a codebase.
            Use the following context to answer the question. If the context does not contain the answer, say you don't know.
            Context: {context}
            Question: {query}
            Answer:
        """
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model_name, "prompt": prompt.format(context=context, query=query), "temperature": 0.2},
        )
        response.raise_for_status()
        return response.json().get("response", "")