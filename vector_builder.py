import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import torch

def build_faiss_index(
    data_folder: str = "data", index_path: str = "faiss_index",
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
):
    """
    Load all PDFs from `data_folder`, split into semantic chunks,
    embed them, build a FAISS index, and save it to `index_path`.
    """
    # Initialize embedder with explicit model_name
    device = "cuda" if torch.cuda.is_available() else "cpu"
    embedder = HuggingFaceEmbeddings(model_name=model_name, model_kwargs={"device": device})

    # Aggregate chunks
    all_docs = []
    for fname in os.listdir(data_folder):
        if fname.lower().endswith(".pdf"):
            path = os.path.join(data_folder, fname)
            loader = PDFPlumberLoader(path)
            pages = loader.load()

            splitter = SemanticChunker(embedder)
            chunks = splitter.split_documents(pages)
            for doc in chunks:
                doc.metadata["source"] = fname
            all_docs.extend(chunks)

    if not all_docs:
        raise ValueError(f"No PDF files found in {data_folder}")

    # Build FAISS index
    vector_index = FAISS.from_documents(all_docs, embedder)

    # Persist to disk
    os.makedirs(index_path, exist_ok=True)
    vector_index.save_local(index_path)
    print(f"FAISS index built and saved at '{index_path}'")


if __name__ == "__main__":
    build_faiss_index()

