# scripts/sync_and_ingest.py

import sys
from pathlib import Path
import traceback
import time

# Ensure `src` is on sys.path so local packages can be imported when running from scripts/
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ingestion.sync.github_service import GithubSyncService
from ingestion.pipeline import run_ingestion
from app.config import GITHUB_REPOS


def main():
    start_time = time.time()

    print("🚀 Iniciando sync + ingest pipeline\n")

    base_clone_dir = Path("repositories")
    base_clone_dir.mkdir(exist_ok=True)

    sync_service = GithubSyncService(base_clone_dir=base_clone_dir)

    for repo_config in GITHUB_REPOS:
        try:
            print(f"🔄 Sincronizando {repo_config.name}...")

            sync_result = sync_service.sync(repo_config)

            print(f"✅ Sync concluído: {repo_config.name}")
            print(f"   Commit: {sync_result.version}\n")

            run_ingestion(
                repo_name=sync_result.name,
                local_path=sync_result.local_path,
                commit_hash=sync_result.version
            )

        except Exception as e:
            print(f"❌ Erro ao processar {repo_config.name}")
            print(str(e))
            traceback.print_exc()

    total_time = time.time() - start_time
    print(f"\n🏁 Pipeline finalizada em {total_time:.2f} segundos")


if __name__ == "__main__":
    main()