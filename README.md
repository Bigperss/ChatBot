# ChatBot# CLI Chatbot — Local LLMs via Ollama + Dynamic Personas

This project is a terminal-based chatbot built in Python that uses locally running LLMs via [Ollama](https://ollama.com) and supports dynamic personas, message history, and token management with streaming output.

---

## Features

- **Local model support** via Ollama (`llama3`, `mistral`, `dolphin`, etc.)
- **Dynamic personas** with name, tone, and formatting control
- **Streaming output** (token-by-token like ChatGPT)
- Fully configurable via `config.yml`

---

## Prerequisites

Make sure you have the following installed:

- **[Miniconda or Anaconda](https://docs.conda.io/en/latest/miniconda.html)** for environment management
- **[Ollama](https://ollama.com/download)** running locally (`ollama run llama3`)
- Python ≥ 3.10

---

## Installation

```bash
# Clone the repository
git clone git@github.com:Bigperss/ChatBot.git
cd ChatBot

# Create the environment
conda env create -f environment.yml
conda activate chatbot

# Run the chatbot
python chatbot -model llama3 -persona dev
```

## Available Commands

```bash
python chatbot.py -model llama3 -persona dev
python chatbot.py -list  # List available personas
```

Use `/bye` in the chat to end the session.

---

## 🧠 Config: `config.yml`

```yaml
model: llama3.1:latest
max_token: 1000
default_persona: none

personas:
  gentle:
    description: You are a kind and supportive assistant. You explain things clearly and simply, always using a friendly and encouraging tone. Your goal is to make the user feel understood and confident.
    name: Gabriel
  dev:
    description: You are a technical assistant specialized in software development. You provide concise, accurate, and professional answers. You give clear code examples when relevant.
    format: |
      Always respond with a JSON object using the following structure:
      {
        "reply": "<your answer here>",
        "explanation": "<a short explanation of the reasoning>",
        "context": "<optional context if needed>"
      }
      Only output valid JSON. Do not add any commentary or formatting outside of the JSON object.
  sarcastic:
    description: You are a sarcastic assistant who answers questions with dry wit and irony. You still provide correct information, but with a humorous, sometimes passive-aggressive tone. You make fun of obvious questions but still help.
    name: Jonathan
```

> You can customize or add more personas here!

## Troubleshooting

- **Model not available?**
  Run: `ollama run llama3.1`

---

## Author

Built by Charles Faudou.