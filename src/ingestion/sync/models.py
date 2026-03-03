from pathlib import Path
from dataclasses import dataclass

@dataclass
class SyncResult:
    name: str
    local_path: Path
    version: str
    
    
@dataclass
class SyncConfig:
    name: str
    url: Path
    branch: str
    repo_type: str