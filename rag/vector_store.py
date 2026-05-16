from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os


def create_vector_store(chunks):
    embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="db"
    )

    return vectorstore