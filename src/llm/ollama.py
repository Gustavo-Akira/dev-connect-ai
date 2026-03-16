import json

import requests

from llm.models import QueryResult
from .client import LLMClient
from ollama import chat

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
        try:
            response = chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt.format(context=context, query=query)}],
                stream=True,
            )
        except requests.RequestException:
            return QueryResult(response="", prompt_tokens=0, completion_tokens=0)

        answer = ""
        prompt_tokens = 0
        completion_tokens = 0

        for line in response:
            msg = line.message.content
            answer += msg
            prompt_tokens = line.prompt_eval_count
            completion_tokens = line.eval_count

        return QueryResult(
            response=answer.strip(),
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens
        )