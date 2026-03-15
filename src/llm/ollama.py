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
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json={"model": self.model_name, "messages": [{"role": "user", "content": prompt.format(context=context, query=query)}]},
                stream=True,
            )
        except requests.RequestException:
            return QueryResult(response="", prompt_tokens=0, completion_tokens=0)

        answer = ""
        prompt_tokens = 0
        completion_tokens = 0

        for line in response.iter_lines(decode_unicode=True):
            if not line:
                continue
            try:
                data = json.loads(line)
            except (ValueError, json.JSONDecodeError):
                continue

            if not isinstance(data, dict):
                continue

            msg = data.get("message")
            if isinstance(msg, dict):
                content = msg.get("content")
                if isinstance(content, str):
                    answer += content

            p = data.get("prompt_eval_count")
            e = data.get("eval_count")
            try:
                if p is not None:
                    prompt_tokens = int(p)
            except (TypeError, ValueError):
                pass
            try:
                if e is not None:
                    completion_tokens = int(e)
            except (TypeError, ValueError):
                pass

        return QueryResult(
            response=answer.strip(),
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens
        )