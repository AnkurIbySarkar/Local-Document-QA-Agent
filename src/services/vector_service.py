import os
import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from src.core.interfaces import RetrieverInterface,  EmbeddingsInterface
from src.core.config import EMBEDDING_MODEL, DB_LOCATION, COLLECTION_NAME

class ChromaRetriever(RetrieverInterface):
    def __init__(self, embedding_service: EmbeddingsInterface):
        self.embedding_service = embedding_service
        self.vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=DB_LOCATION,
            embedding_function=self.embedding_service.model
        )
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 5})

    def ingest_file(self, file_path: str):
        """Load and embed any supported document (CSV, TXT, PDF)."""
        ext = os.path.splitext(file_path)[-1].lower()
        documents, ids = [], []

        if ext == ".csv":
            df = pd.read_csv(file_path)
            for i, row in df.iterrows():
                text = " ".join([str(x) for x in row.values])
                documents.append(Document(page_content=text, id=str(i)))
                ids.append(str(i))
        elif ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    documents.append(Document(page_content=line.strip(), id=str(i)))
                    ids.append(str(i))
        elif ext == ".pdf":
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                documents.append(Document(page_content=text, id=str(i)))
                ids.append(str(i))
        else:
            raise ValueError(f"Unsupported file format: {ext}")

        self.vector_store.add_documents(documents=documents, ids=ids)

    def retrieve(self, query: str):
        results = self.retriever.invoke(query)
        return [doc.page_content for doc in results]
