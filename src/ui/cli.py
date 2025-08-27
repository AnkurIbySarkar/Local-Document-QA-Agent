from services.llm_service import OllamaService
from services.vector_service import ChromaRetriever
from core.config import MODEL_NAME

def run_cli():
    llm = OllamaService(MODEL_NAME)
    retriever = ChromaRetriever()

    while True:
        print("\n-------------------------------")
        question = input("Ask your question (q to quit): ")
        if question.lower() == "q":
            break

        reviews = retriever.retrieve(question)
        result = llm.generate(reviews, question)
        print("\nAnswer:", result)