import os
import openai
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from datetime import datetime

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
es = Elasticsearch(os.getenv("ELASTIC_URL"))
index = os.getenv("ELASTIC_INDEX")

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response['choices'][0]['message']['content']
    
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": answer
    }
    es.index(index=index, body=log_entry)

    return answer

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        reply = ask_gpt(user_input)
        print(f"GPT: {reply}")
