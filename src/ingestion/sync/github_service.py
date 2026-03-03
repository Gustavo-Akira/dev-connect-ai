
from pathlib import Path

from git import Repo

from ingestion.sync.service import SyncService, SyncResult


class GithubSyncService(SyncService):

    def __init__(self, base_clone_dir: Path):
        self.base_clone_dir = base_clone_dir

    def sync(self, repo_config):
        local_path = self.base_clone_dir / repo_config.name

        if not local_path.exists():
            repo = Repo.clone_from(repo_config.url, local_path)
        else:
            repo = Repo(local_path)
            repo.remotes.origin.pull()

        return SyncResult(
            name=repo_config.name,
            local_path=local_path,
            version=repo.head.commit.hexsha
        )