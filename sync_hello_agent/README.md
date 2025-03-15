# Sync Hello Agent

A synchronous agent implementation using the OpenAI Agents SDK and Gemini API.

## 📋 Description

This project demonstrates how to create synchronous agents that leverage both OpenAI's Agents SDK and Google's Gemini API. It provides a foundation for building intelligent agents that can perform tasks with a simple synchronous architecture.

## ✨ Features

- Synchronous execution of agent tasks
- Integration with Google's Gemini API
- Built on OpenAI's Agents SDK
- Clean and straightforward implementation

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- UV package manager (recommended)
- Gemini API key

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/sync-hello-agent.git
cd sync-hello-agent
```

2. **Set up a virtual environment**

UV is recommended for package management:

```bash
# Install UV if not already installed
pip install uv

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
uv add openai-agents python-dotenv.
```

4. **Configure API keys**

Create a `.env` file in the project root with the following:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🔧 Usage

Run the main script:

```bash
uv run main.py
```

This will execute a simple synchronous agent conversation using Gemini's LLM.

## 🧩 How It Works

The `sync_hello_agent` uses the `Runner.run_sync()` method from the OpenAI Agents SDK to process requests synchronously. This approach is simpler than the asynchronous implementation and is perfect for straightforward use cases where asynchronous processing isn't required.

## 📄 License

[MIT](LICENSE)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!


