from ingestion.sync.models import SyncConfig


GITHUB_REPOS = [
    SyncConfig(
        name="devconnect",
        url="https://github.com/Gustavo-Akira/devconnect",
        branch="main",
        repo_type="backend"
    ),
    SyncConfig(
        name="devconnect-frontend",
        url="https://github.com/Gustavo-Akira/devconnect-frontend",
        branch="main",
        repo_type="frontend"
    ),
    SyncConfig(
        name="dev-connect-mobile",
        url="https://github.com/Gustavo-Akira/dev-connect-mobile",
        branch="main",
        repo_type="mobile"
    ),
    SyncConfig(
        name="devconenct-storage",
        url="https://github.com/Gustavo-Akira/devconenct-storage",
        branch="main",
        repo_type="backend"
    ),
    SyncConfig(
        name="dev-connect-relations",
        url="https://github.com/Gustavo-Akira/dev-connect-relations",
        branch="main",
        repo_type="backend"
    )
]