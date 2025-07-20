# GPT + ELK Stack Logger

This is a lightweight logging tool that connects OpenAI's GPT model to the ELK stack (Elasticsearch and Kibana). It logs prompts, responses, and relevant metadata, enabling visibility into GPT usage and performance over time.

## What It Does

- Sends prompts to GPT-4 from the command line
- Logs the following data to Elasticsearch:
  - Prompt and response
  - Token counts (prompt, completion, total)
  - Cost estimation in USD
  - Latency in milliseconds
  - Model used
  - Timestamp
- Enables full search and filtering in Kibana
- Supports dashboards for analysis and visualization

## Tech Stack

- Python 3.11
- OpenAI API
- Elasticsearch and Kibana (via Docker Compose)
- `.env`-based configuration

## Getting Started (Local Setup)

### 1. Set up your Python environment

```bash
py -3.11 -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file with the following content:

```
OPENAI_API_KEY=your-api-key
ELASTIC_URL=http://localhost:9200
ELASTIC_INDEX=gpt-logs
```

### 3. Start the ELK stack

```bash
docker-compose up -d
```

Wait a minute or two for Elasticsearch and Kibana to become ready.

### 4. Run the logger

```bash
python app.py
```

You’ll be prompted in the terminal. Each request will be sent to GPT-4 and logged to Elasticsearch.

## Kibana Dashboards

Use Kibana to build dashboards based on fields like:

- Average latency (`latency_ms`)
- Token usage trends (`prompt_tokens`, `completion_tokens`, `total_tokens`)
- Total and average cost (`cost_usd`)
- Requests per day or month

You can build visualizations using Kibana Lens, then save them to a dashboard. This enables cost tracking, performance insights, and usage auditing over time.



![Kibana Dashboard](https://raw.githubusercontent.com/asrahmann/gpt-elk-logger/main/assets/kibana_dashboard.png)

## Future Plans

- Web UI or chatbot interface
- Prebuilt Kibana dashboards
- Optional Logstash integration
  Note: A basic logstash.conf is included for future development, but the current setup sends logs directly from Python to Elasticsearch for simplicity.
- Dockerized app version for easier deployment
