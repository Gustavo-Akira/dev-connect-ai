from pathlib import Path

from ingestion.file_filter import filter_files

def run_ingestion(repo_name: str, local_path: Path, commit_hash: str):
    print(f"[INGEST] Repo: {repo_name}")
    print(f"[INGEST] Commit: {commit_hash}")
    print(f"[INGEST] Path: {local_path}")
    for file_path in local_path.rglob("*"):
        if file_path.is_file() and filter_files(file_path):
            print(f"[INGEST] Processando: {file_path}")

    print(f"[INGEST] Finalizado: {repo_name}")