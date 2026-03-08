from ingestion.sync.models import SyncConfig
import os
from dotenv import load_dotenv

load_dotenv()

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

QDRANT_HOST=os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT=int(os.getenv("QDRANT_PORT", "6333"))
QDRANT_COLLECTION_NAME=os.getenv("QDRANT_COLLECTION_NAME", "devconnect")

EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

CONTEXT_MAX_SIZE=int(os.getenv("CONTEXT_MAX_SIZE", "2048"))