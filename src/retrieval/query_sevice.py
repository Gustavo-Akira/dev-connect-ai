from embeddings.service import EmbeddingService
from llm.client import LLMClient
from retrieval.context_builder import ContextBuilder
from retrieval.models import QueryResponse
from vectorstore.store import VectorStore


class QueryService:
    def __init__(self, vector_store: VectorStore, llm: LLMClient, context_builder: ContextBuilder, embedding_service: EmbeddingService):
        self.vector_store = vector_store
        self.llm = llm
        self.context_builder = context_builder
        self.embedding_service = embedding_service

    def query(self, query_text):
        query_vector = self.embedding_service.embed(query_text)
        results = self.vector_store.search(query_vector, top_k=5)

        context = self.context_builder.build_context(results)
        answer = self.llm.generate_response(query_text, context)
        response = QueryResponse(
            sources=[result.metadata.get("file_path", "unknown") for result in results],
            response=answer
        )
        return response