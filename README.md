# DF\_RAG – Retrieval-Augmented Generation for Digital Forensics

DF\_RAG is a Retrieval-Augmented Generation (RAG) solution designed specifically to streamline knowledge retrieval from PDF documents for digital forensic investigations. Built using LangChain, FAISS, HuggingFace models, and Streamlit, DF\_RAG provides forensic analysts with a user-friendly interface for asking natural-language questions directly to their digital knowledge base.

---

## 🌟 Features

* **Semantic Search**: Quickly retrieve relevant information from hundreds of PDF documents.
* **Local Operation**: Runs entirely locally—no sensitive data leaves your machine.
* **Interactive UI**: Simple Streamlit app interface—no coding required.
* **Dynamic Indexing**: Easily refresh your knowledge database by adding new PDF files.

---

## 🚀 Getting Started

Follow these instructions to set up and run DF\_RAG locally.

### Prerequisites

Ensure you have these installed on your system:

* [Docker](https://www.docker.com/get-started/) (required)
* Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/INsig2/Digital-Forensics-RAG.git
cd Digital-Forensics-RAG
```

### Step 2: Populate the Data Folder

Place your PDF documents into the `data` directory. This folder is initially empty and ready for your data.

```
Digital-Forensics-RAG/
└── data/
    ├── example1.pdf
    └── example2.pdf
```

---

## 🐳 Docker Setup and Running

Docker simplifies installation and ensures consistent performance across different systems.

### Option 1: Auto-Rebuild at Build Time

By default, the Dockerfile will attempt to automatically build the vector index when you build the container:

```bash
docker build -t df_rag_app .
docker run -p 8501:8501 df_rag_app
```

> Note: If the `data/` folder is empty during build, the build will continue, and you can rebuild later using the Streamlit UI.

### Option 2: Rebuild via the Streamlit UI

Once the app is running, simply:

1. Add new PDFs to the `data` directory.
2. Use the sidebar and click **"Rebuild index from PDFs"**.
3. The FAISS index will be regenerated dynamically.

---

## 📖 How to Use

* Open the Streamlit app in your browser.
* Type a natural-language question into the input box.
* Receive direct, context-aware answers sourced from your PDFs.

---

## ♻️ Refreshing the Index

You can rebuild the index using either method:

### 🧱 Build-Time (Docker)

* Stop the container.
* Add new PDFs.
* Rebuild:

```bash
docker build -t df_rag_app .
docker run -p 8501:8501 df_rag_app
```

### 🔁 Runtime (Streamlit UI)

* Add new PDFs.
* Open the app.
* Click "Rebuild index from PDFs" in the sidebar.

---

## 🌐 Versatility

Although initially designed for digital forensics, DF\_RAG can handle PDF documents from any field or topic. Simply add PDFs of your choice into the `data` folder, and the system will efficiently handle semantic queries for any domain-specific content.

---

## 🔗 Useful Resources

* [LangChain Documentation](https://python.langchain.com/docs/introduction/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Hugging Face Sentence Transformers](https://www.sbert.net/)
* [Ollama](https://ollama.com/)
* [Streamlit](https://streamlit.io/)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author and Maintainer

Developed by Marija Dragošević  
[LinkedIn](https://www.linkedin.com/in/marija-drago%C5%A1evi%C4%87-800919294/)

---

Happy querying! 🚀🔍📚
