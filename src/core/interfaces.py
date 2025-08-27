from abc import ABC, abstractmethod
from typing import List, Dict, Any

class EmbeddingsInterface(ABC):
    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Return embeddings for a list of texts"""
        pass

class RetrieverInterface(ABC):
    @abstractmethod
    def retrieve(self, query: str) -> List[str]:
        pass

class LLMInterface(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass