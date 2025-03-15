# LLM Configuration at Run Level

![OpenAI Agents SDK](https://img.shields.io/badge/OpenAI-Agents%20SDK-000000?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-4B8BBE?style=for-the-badge&logo=python&logoColor=white)

## 🏃 Overview

This project demonstrates how to configure a Large Language Model (LLM) at the **run level** using the OpenAI Agents SDK. This approach allows for maximum flexibility, letting you change model configuration for each individual run without modifying your agent definitions.

## ✨ Features

- Configures the LLM at run time using a RunConfig object
- Uses Gemini 1.5 Flash model through OpenAI compatible API
- Separates agent definition from model configuration
- Implements synchronous execution with `run_sync`

## 🛠️ Installation

```bash
# Clone the repository
git clone <repository-url>
cd conf_llm_run_level

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

The agent will respond to a greeting prompt using the model configuration specified in the RunConfig.

## 🔄 How It Works

1. Creates an OpenAI client configured to use the Gemini API
2. Creates a model using the client
3. Creates a RunConfig with the model, provider, and tracing settings
4. Defines an agent without specifying a model
5. Runs the agent with a specific prompt and the RunConfig
6. Displays the agent's response

## 💡 When to Use Run-Level Configuration

Run-level configuration is ideal when:
- You need to dynamically switch between different models for the same agent
- You want to experiment with different model parameters without changing agent code
- Your application needs to adapt LLM settings based on context or user preferences
- You have a microservices architecture where configuration might come from different sources

## 📊 Comparison with Other Configuration Approaches

| Configuration Level | Flexibility | Reusability | Use Case |
|---------------------|-------------|-------------|----------|
| Agent Level | Low | High | When agent personality is tied to specific model settings |
| Global Level | Medium | High | When using consistent settings across application |
| Run Level | High | Medium | When needing dynamic configuration per interaction |

## 📚 Further Learning

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-python)

