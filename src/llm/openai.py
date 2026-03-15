import os

from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_MODEL
from llm.models import QueryResult
from .client import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        
    def generate_response(self, query: str, context: str) -> QueryResult:
        prompt = """
            You are an assistant helping developers understand a codebase.
            Use the following context to answer the question. If the context does not contain the answer, say you don't know.
            Context: {context}
            Question: {query}
            Answer:
        """
        
        response = self.client.chat.completions.create(
            model = OPENAI_MODEL,
            messages = [
                {"role": "user", "content": prompt.format(context=context, query=query)}
            ],
            temperature=0.2
        )
        
        return QueryResult(
            response=response.choices[0].message.content.strip(),
            prompt_tokens=response.usage.prompt_tokens,
            completion_tokens=response.usage.completion_tokens
        )