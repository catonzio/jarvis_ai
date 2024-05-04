import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Scrivimi un breve racconto su un gatto e un topo."}
    ],
)

print(response["message"]["content"])
