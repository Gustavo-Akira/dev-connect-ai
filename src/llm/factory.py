from app.config import LLM_PROVIDER, OLLAMA_MODEL
from llm.client import LLMClient
from llm.ollama import OllamaClient
from llm.openai import OpenAIClient

class LLMFactory:
    
    @staticmethod
    def create_llm_client() -> LLMClient:
        llm = LLM_PROVIDER.lower()
        if llm == "ollama":
            model_name= OLLAMA_MODEL
            return OllamaClient(model_name=model_name)
        elif llm == "openai":
            return OpenAIClient()
        else:
            raise ValueError(f"Unsupported LLM provider: {llm}")