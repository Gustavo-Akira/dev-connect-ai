from pathlib import Path

from embeddings.service import EmbeddingService
from ingestion.chunk.chunk_builder import ChunkBuilder
from ingestion.chunk.factory import ChunkerFactory
from ingestion.file_filter import filter_files

def run_ingestion(repo_name: str, local_path: Path, commit_hash: str):
    print(f"[INGEST] Repo: {repo_name}")
    print(f"[INGEST] Commit: {commit_hash}")
    print(f"[INGEST] Path: {local_path}")
    builder = ChunkBuilder()
    embedding_service = EmbeddingService()
    for file_path in local_path.rglob("*"):
        if file_path.is_file() and filter_files(file_path):
            chunker = ChunkerFactory().get_chunker(file_path)
            if chunker is None:
                print(f"[INGEST] Ignorando {file_path} (sem chunker suportado)")
                continue
            raw_chunks = chunker.chunk(file_path, file_path.read_text(encoding="utf-8"))
            chunks = builder.build(file_path, repo_name, raw_chunks)
            texts = [c.text for c in chunks]
            vectors = embedding_service.embed_batch(texts)
            print(f"[INGEST] {file_path}: {len(vectors)} vetores gerados")
    print(f"[INGEST] Finalizado: {repo_name}")