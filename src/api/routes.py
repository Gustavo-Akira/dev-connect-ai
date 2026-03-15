from fastapi import APIRouter

from api.schemas import QueryRequest
from api.schemas import QueryResponse
from embeddings.service import EmbeddingService
from llm.factory import LLMFactory
from retrieval.context_builder import ContextBuilder
from retrieval.query_sevice import QueryService
from vectorstore.qdrant import QdrantVectorStore

router = APIRouter()
vector_store = QdrantVectorStore()
llm_client =  LLMFactory.create_llm_client()
context_builder = ContextBuilder()
embedding_service= EmbeddingService()
query_service = QueryService(vector_store, llm_client, context_builder=context_builder,embedding_service=embedding_service)

@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    response = query_service.query(request.question)
    return QueryResponse(answer=response.response, sources=response.sources, completion_tokens=response.completion_tokens, prompt_tokens=response.prompt_tokens)