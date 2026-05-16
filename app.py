from rag.qa_chain import ask_llm
from rag.retriever import retrieve_docs
from rag.vector_store import create_vector_store
from rag.text_splitter import split_documents
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
import json
import os
from openai import OpenAI
from rag.pdf_loader import load_pdf
if os.path.exists("chat_history.json"):
    with open("chat_history.json", "r", encoding="utf-8") as f:
        chat_history = json.load(f)
else:
    chat_history = []

st.sidebar.title("控制面板")

temperature = st.sidebar.slider(
    "AI创造力",
    0.0,
    1.5,
    0.7
)

model_name = st.sidebar.selectbox(
    "选择模型",
    [
        "deepseek-chat",
        "deepseek-reasoner"
    ]
)

if st.sidebar.button("🗑 清空聊天"):
    st.session_state.messages = []
    st.rerun()              
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

st.title("我的AI聊天机器人")
query = st.text_input("请输入你的问题")
uploaded_file = st.file_uploader("上传PDF文件", type=["pdf"])
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    docs = load_pdf("temp.pdf")

    chunks = split_documents(docs)

    vectorstore = create_vector_store(chunks)

    if query:
        results = retrieve_docs(vectorstore, query)

        answer = ask_llm(query, results)

        st.write(answer)

    response = client.chat.completions.create(
        model=model_name,

        messages=[
            {
                "role": "system",
                "content": "你是一个专业、聪明、友好的中文AI助手"
            },

        ],

        temperature=temperature,
        stream=False,
    )
