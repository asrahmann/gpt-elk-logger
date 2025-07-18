# GPT + ELK Stack Logger (🚧 Under Construction)

This is a simple proof-of-concept project that integrates OpenAI's GPT model with the ELK stack (Elasticsearch, Logstash, Kibana) for logging and visualizing AI prompts and responses.

## 📌 Purpose

The goal is to:
- Interact with OpenAI's GPT model via a basic terminal interface
- Log both the prompt and GPT response to Elasticsearch
- Visualize the conversation flow using Kibana dashboards
- Lay the groundwork for future chatbot integrations (Discord, Web UI, etc.)

## 🧱 Stack

- **Python 3.11**
- **OpenAI API (GPT-4)**
- **Elasticsearch**
- **Kibana**
- *(Optional)* Logstash for advanced ingestion logic
- **Docker Compose** for local ELK stack setup
- **.env** file for configuration and API keys

## 🛠️ Status

> ⚠️ This project is **under construction** and currently only includes a CLI-based prototype. Additional features like chatbot integration, web API access, and auto-scaling logging pipelines are planned.

## 🔐 Local Development

```bash
# Create virtual environment
py -3.11 -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start ELK stack (requires Docker)
docker-compose up -d

# Run the app
python app.py
