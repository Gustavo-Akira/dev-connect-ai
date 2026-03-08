from vectorstore.model import SearchResult


class ContextBuilder:
    
    
    def __init__(self, max_length=2048):
        self.max_length = max_length

    def build_context(self, results: list[SearchResult]) -> str:
        context = ""
        for result in results:
            if len(context) + len(result.text) <= self.max_length:
                context += result.text + "\n"
            else:
                break
        return context.strip()