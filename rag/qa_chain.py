from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def ask_llm(query, results):
    context = "\n".join([doc.page_content for doc in results])

    prompt = f"""
你是一名AI文档助手。

请基于下面内容回答问题。

文档内容：
{context}

用户问题：
{query}
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content