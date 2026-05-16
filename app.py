import streamlit as st
import json
import os
from openai import OpenAI
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
    api_key="sk-68c71166dc1b4547acb17d0307214251",
    base_url="https://api.deepseek.com"
)

st.title("我的AI聊天机器人")
uploaded_file = st.file_uploader(
    "上传txt文件",
    type=["txt"]
)
if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")
    st.success("文件上传成功")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("请输入内容")
full_response = "" 
if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    chat_history.append(
        {"role": "user", "content": user_input}
    )
    st.chat_message("user").write(user_input)

    

    response = client.chat.completions.create(
        model=model_name,

        messages=[
            {
                "role": "system",
                "content": "你是一个专业、聪明、友好的中文AI助手"
            },

            {
                "role": "system",
                "content": file_content if uploaded_file else ""
            },

            *st.session_state.messages
        ],

        temperature=temperature,
        stream=False,
    )
    
    message_placeholder = st.empty()
        
    full_response = response.choices[0].message.content

    st.chat_message("assistant").write(full_response)
        
    st.session_state.messages.append(
    {"role": "assistant", "content": full_response}
)

chat_history.append(
    {"role": "assistant", "content": full_response}
)

with open("chat_history.json", "w", encoding="utf-8") as f:
    json.dump(chat_history, f, ensure_ascii=False, indent=4)
        