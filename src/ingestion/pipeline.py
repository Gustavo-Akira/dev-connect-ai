from pathlib import Path

def run_ingestion(repo_name: str, local_path: Path, commit_hash: str):
    print(f"[INGEST] Repo: {repo_name}")
    print(f"[INGEST] Commit: {commit_hash}")
    print(f"[INGEST] Path: {local_path}")


    print(f"[INGEST] Finalizado: {repo_name}")