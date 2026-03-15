import json

import requests

from llm.models import QueryResult
from .client import LLMClient

class OllamaClient(LLMClient):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.base_url = "http://localhost:11434"

    def generate_response(self, query: str,context: str) -> QueryResult:
        prompt = """
            You are an assistant helping developers understand a codebase.
            Use the following context to answer the question. If the context does not contain the answer, say you don't know.
            Context: {context}
            Question: {query}
            Answer:
        """
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={"model": self.model_name, "messages": [{"role": "user", "content": prompt.format(context=context, query=query)}]},
        )
        answer = ""

        for line in response.iter_lines():
            if line:
                data = json.loads(line)
            if "message" in data:
                answer += data["message"]["content"]

        return QueryResult(
            response=answer.strip(),
            prompt_tokens=0,
            completion_tokens=0
        )