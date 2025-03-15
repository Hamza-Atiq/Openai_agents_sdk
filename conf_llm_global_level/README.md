# LLM Configuration at Global Level

![OpenAI Agents SDK](https://img.shields.io/badge/OpenAI-Agents%20SDK-000000?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-4B8BBE?style=for-the-badge&logo=python&logoColor=white)

## 🌐 Overview

This project demonstrates how to configure a Large Language Model (LLM) at the **global level** using the OpenAI Agents SDK. By setting a default OpenAI client globally, you can ensure consistent model behavior across multiple agents or throughout your application.

## ✨ Features

- Sets a global default OpenAI client for all agents
- Uses Gemini 1.5 Flash model through OpenAI compatible API
- Disables tracing globally for more efficient performance
- Implements synchronous execution with `run_sync`

## 🛠️ Installation

```bash
# Clone the repository
git clone <repository-url>
cd conf_llm_global_level

#UV is recommended for package management:
pip install uv

# Set up a virtual environment
uv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
uv add openai-agents python-dotenv
```

## 🔑 Environment Setup

Create a `.env` file in the root directory with your API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🚀 Usage

Run the example with:

```bash
uv run main.py
```

The agent will respond to the prompt "Hello, how are you?" using the globally configured model.

## 🔄 How It Works

1. Creates an OpenAI client configured to use the Gemini API
2. Sets this client as the default at the global level with `set_default_openai_client`
3. Disables tracing globally for all operations
4. Creates a model using the globally configured client
5. Creates an agent with the model and runs it
6. Displays the agent's response

## 💡 When to Use Global Configuration

Global configuration is ideal when:
- You need consistent model behavior across multiple agents
- Your application uses the same LLM configuration throughout
- You want to reduce repetitive configuration code

## 📚 Further Learning

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-python)
