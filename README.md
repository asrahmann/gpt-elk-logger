# GPT + ELK Stack Logger (Under Construction)

This is a basic logging tool that connects OpenAI's GPT model to the ELK stack (Elasticsearch and Kibana, optionally Logstash). It logs every prompt and response so you can visualize GPT behavior over time.

## What it does

- Sends prompts to GPT-4 from the command line
- Logs both the prompt and the GPT response to Elasticsearch
- Creates a searchable history of interactions
- Future plans include hooking it into a chatbot or a simple web UI

## Tech Stack

- Python 3.11
- OpenAI API
- Elasticsearch and Kibana
- Docker Compose
- `.env`-based configuration

## Getting Started (Local Setup)

```bash
# Set up virtual environment
py -3.11 -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start ELK stack (Docker required)
docker-compose up -d

# Run the app
python app.py

