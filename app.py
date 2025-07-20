import os
import openai
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from datetime import datetime

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
es = Elasticsearch(os.getenv("ELASTIC_URL"))
index = os.getenv("ELASTIC_INDEX")

# Cost per 1,000 tokens based on model
MODEL_PRICING = {
    "gpt-4": {"prompt": 0.03, "completion": 0.06},
    "gpt-4-0613": {"prompt": 0.03, "completion": 0.06},
    "gpt-3.5-turbo": {"prompt": 0.0015, "completion": 0.002},
    "gpt-3.5-turbo-0613": {"prompt": 0.0015, "completion": 0.002}
}

def ask_gpt(prompt, user_id="navi", source="terminal"):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": prompt}]
    )

    model = response.model
    usage = response.usage
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    # Cost calculation
    price_info = MODEL_PRICING.get(model, {"prompt": 0, "completion": 0})
    cost = (prompt_tokens / 1000) * price_info["prompt"] + (completion_tokens / 1000) * price_info["completion"]

    answer = response['choices'][0]['message']['content']

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": answer,
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
        "cost_usd": round(cost, 6),
        "user_id": user_id,
        "source": source,
        "status": "success"
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
