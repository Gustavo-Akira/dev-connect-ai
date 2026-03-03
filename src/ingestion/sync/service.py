
from abc import ABC, abstractmethod

from ingestion.sync.models import SyncConfig, SyncResult


class SyncService(ABC):
    @abstractmethod
    def sync(self, configs: SyncConfig) -> SyncResult:
        pass