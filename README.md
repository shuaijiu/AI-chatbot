# AI RAG Knowledge Base Assistant

## 项目介绍

这是一个基于 RAG（检索增强生成）的 AI 知识库问答系统。

用户上传 PDF 文件后，系统会：

- 自动解析 PDF
- 文本 Chunk 切分
- 向量化 Embedding
- 存入 Chroma 向量数据库
- 进行语义检索
- 使用 DeepSeek 大模型生成回答

## 技术栈

- Python
- Streamlit
- LangChain
- ChromaDB
- DeepSeek API
- OpenAI SDK

## 项目功能

- PDF知识库上传
- RAG检索增强问答
- 向量数据库构建
- Chunk文本切分
- AI智能问答

## 项目启动

```bash
pip install -r requirements.txt
streamlit run app.py