import re

from pathlib import Path

from ingestion.chunk.base import BaseChunker

class GoChunker(BaseChunker):
    FUNC_PATTERN = re.compile(r'\nfunc\s+\(?.*\)?\s*\w+\(')
    
    def supports(self, file_path: Path) -> bool:
        return file_path.suffix.lower() == '.go'
    
    def chunk(self, file_path: Path, content: str) -> list[str]:
        chunks = []
        last_index = 0
        
        for match in self.FUNC_PATTERN.finditer(content):
            start_index = match.start()
            if last_index < start_index:
                chunks.append(content[last_index:start_index].strip())
            last_index = start_index
        
        if last_index < len(content):
            chunks.append(content[last_index:].strip())
        
        return [chunk for chunk in chunks if chunk]