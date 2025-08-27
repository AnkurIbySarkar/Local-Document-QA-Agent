from langchain_ollama import OllamaEmbeddings
from src.core.interfaces import EmbeddingsInterface
from typing import List

class OllamaEmbeddingService(EmbeddingsInterface):
    def __init__(self, model_name: str):
        self.model = OllamaEmbeddings(model=model_name)

    def embed(self, texts: List[str]) -> List[List[float]]:
        return self.model.embed_documents(texts)