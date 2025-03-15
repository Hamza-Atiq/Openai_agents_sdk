# LLM Configuration at Agent Level

![OpenAI Agents SDK](https://img.shields.io/badge/OpenAI-Agents%20SDK-000000?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-4B8BBE?style=for-the-badge&logo=python&logoColor=white)

## 🚀 Overview

This project demonstrates how to configure a Large Language Model (LLM) at the **Agent level** using the OpenAI Agents SDK. It shows how to create custom agents with specific personalities or behavior patterns by configuring the model directly within the Agent instance.

## ✨ Features

- Uses Gemini 1.5 Flash model through OpenAI compatible API
- Configures the LLM at the agent level for fine-grained control
- Demonstrates setting custom agent instructions ("You only respond in haiku")
- Uses async functionality for efficient execution

## 🛠️ Installation

```bash
# Clone the repository
git clone <repository-url>
cd conf_llm_agent_level

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

The agent will respond to the prompt "Write me a haiku about a cat" with a haiku, demonstrating how the model configuration at the agent level affects the response.

## 🔄 How It Works

1. Creates an OpenAI client configured to use the Gemini API
2. Configures the model directly in the Agent initialization
3. Sets specific instructions for response style (haiku format)
4. Runs the agent with a specific prompt
5. Displays the agent's response

## 📚 Further Learning

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-python)

