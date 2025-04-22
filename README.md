# ChatBot# CLI Chatbot — Local LLMs via Ollama + Dynamic Personas

This project is a terminal-based chatbot built in Python that uses locally running LLMs via [Ollama](https://ollama.com) and supports dynamic personas, message history, and token management with streaming output.

---

## Features

- **Local model support** via Ollama (`llama3`, `mistral`, `dolphin`, etc.)
- **Dynamic system personas** (gentle, dev, sarcastic, etc.)
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

---

## Project Structure

```
chatbot-cli/
├── chatbot              # Entry point CLI
├── config.yml           # Main configuration file
├── src/
│   └── bot.py           # Bot logic (streaming, history, token check)
├── environment.yml      # Conda environment setup
```

---

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
  gentle: You are a kind and supportive assistant...
  dev: You are a technical assistant...
  sarcastic: You are a sarcastic assistant...
```

> You can customize or add more personas here!

## Troubleshooting

- **Model not available?**
  Run: `ollama run llama3`

---

## Author

Built by Charles Faudou.