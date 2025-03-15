# Async Hello Agent

An asynchronous agent implementation using the OpenAI Agents SDK and Gemini API.

## 📋 Description

This project demonstrates how to create asynchronous agents that leverage both OpenAI's Agents SDK and Google's Gemini API. It provides a foundation for building intelligent agents that can perform tasks asynchronously.

## ✨ Features

- Asynchronous execution of agent tasks
- Integration with Google's Gemini API
- Built on OpenAI's Agents SDK
- Simple and extensible architecture

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- UV package manager (recommended)
- Gemini API key

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/async-hello-agent.git
cd async-hello-agent
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
uv add openai-agents python-dotenv
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

## 📄 License

[MIT](LICENSE)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
