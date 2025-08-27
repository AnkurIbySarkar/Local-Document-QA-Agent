from langchain_ollama import OllamaLLM
from src.core.interfaces import LLMInterface
from langchain_core.prompts import ChatPromptTemplate

class OllamaService(LLMInterface):
    def __init__(self, model_name: str):
        self.model = OllamaLLM(model=model_name)
        self.template = ChatPromptTemplate.from_template("""
        You are a helpful assistant that answers questions based on provided documents.

        Documents: {documents}
        Question: {question}
        """)

    def generate(self, documents: str, question: str) -> str:
        chain = self.template | self.model
        return chain.invoke({"documents": documents, "question": question})