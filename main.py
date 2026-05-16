from openai import OpenAI

client = OpenAI(
    api_key="sk-68c71166dc1b4547acb17d0307214251",
    base_url="https://api.deepseek.com"
)

messages = []

while True:
    user_input = input("You: ")

    if user_input == "exit":
        break

    messages.append(
        {"role": "user", "content": user_input}
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    ai_reply = response.choices[0].message.content

    print("AI:", ai_reply)

    messages.append(
        {"role": "assistant", "content": ai_reply}
    )