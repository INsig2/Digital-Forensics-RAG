import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Cache loading of the FAISS index for speed
def load_index(
    index_path: str = "faiss_index",
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
) -> FAISS:
    @st.cache_resource
    def _load():
        embedder = HuggingFaceEmbeddings(model_name=model_name)
        return FAISS.load_local(
            index_path, embedder, allow_dangerous_deserialization=True
        )
    return _load()

# Styling
primary_color = "#1E90FF"
secondary_color = "#FF6347"
background_color = "#F5F5F5"
text_color = "#4561e9"
st.markdown(f"""
    <style>
    .stApp {{ background-color: {background_color}; color: {text_color}; }}
    .stButton>button {{ background-color: {primary_color}; color: white; border-radius: 5px; padding: 10px 20px; }}
    .stTextInput>div>div>input {{ border: 2px solid {primary_color}; border-radius: 5px; padding: 10px; }}
    </style>
""", unsafe_allow_html=True)

st.title("RAG Search over Multiple PDFs")

# Load or build the FAISS index
if not st.sidebar.button("Rebuild index from PDFs"):
    vector_db = load_index()
else:
    from vector_builder import build_faiss_index
    with st.spinner("Rebuilding FAISS index..."):
        build_faiss_index()
    st.rerun()

# Configure retriever with MMR for diversity
retriever = vector_db.as_retriever(
    search_type="mmr", search_kwargs={"k": 5, "fetch_k": 20, "lambda_mult": 0.5}
)

# LLM and prompt setup
llm = Ollama(model="deepseek-r1")
prompt = PromptTemplate.from_template(
    """
    Use the following context to answer. If unknown, say 'I don't know'.
    Context: {context}
    Question: {question}
    """
)

# Build RAG chain via from_chain_type instead of direct constructor
data_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    verbose=True,
    chain_type_kwargs={"prompt": prompt}
)

# Main query box
query = st.text_input("Ask a question across all documents:")
if query:
    with st.spinner("Searching..."):
        result = data_chain(query)
        answer = result["result"]
        sources = {doc.metadata.get("source") for doc in result["source_documents"]}

        st.markdown("**Answer:**")
        st.write(answer)

        st.markdown("**Sources:**")
        for src in sources:
            st.write(f"- {src}")
