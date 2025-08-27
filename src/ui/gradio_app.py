import gradio as gr
from src.services.llm_service import OllamaService
from src.services.vector_service import ChromaRetriever
from src.services.embeddings_service import OllamaEmbeddingService
from src.core.config import MODEL_NAME, EMBEDDING_MODEL

# Dependency Injection
embedding_service = OllamaEmbeddingService(EMBEDDING_MODEL)
retriever = ChromaRetriever(embedding_service)
llm = OllamaService(MODEL_NAME)

def upload_file(file):
    retriever.ingest_file(file.name)
    return f"✅ {file.name} has been ingested!"

def answer_question(question):
    docs = retriever.retrieve(question)
    if not docs:
        return "⚠️ No relevant documents found. Please upload a file first."
    return llm.generate(docs, question)

with gr.Blocks() as demo:
    gr.Markdown("## 📚 Local Document Q&A Assistant")
    with gr.Row():
        file_input = gr.File(label="Upload a document (CSV, TXT, PDF)")
        upload_output = gr.Textbox(label="Ingestion Status")
    upload_button = gr.Button("Ingest Document")
    upload_button.click(upload_file, inputs=[file_input], outputs=[upload_output])

    question = gr.Textbox(label="Ask a question about the documents")
    answer = gr.Textbox(label="Answer")
    ask_button = gr.Button("Get Answer")
    ask_button.click(answer_question, inputs=[question], outputs=[answer])

demo.launch()
