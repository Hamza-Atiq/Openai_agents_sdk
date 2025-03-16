# 🤖 Gemini-Powered Chatbot with Chainlit

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Chainlit](https://img.shields.io/badge/Chainlit-latest-green.svg)
![Agents SDK](https://img.shields.io/badge/Agents_SDK-latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A beautiful, responsive chat interface built with Chainlit and powered by Google's Gemini 2.0 Flash model. This project demonstrates how to create a memory-enabled conversational AI that remembers user information throughout the conversation.

## ✨ Features

- 🚀 Modern, responsive chat UI with Chainlit
- 🧠 Conversation memory that retains user information
- 🔄 Integration with Google's Gemini 2.0 Flash via OpenAI compatibility API
- ⚡ Fast, synchronous conversation processing
- 🧩 Built with the Agents SDK for flexible AI agent implementation

## 📋 Prerequisites

- Python 3.10+
- A Google AI (Gemini) API key
- UV package manager (recommended)

## 🛠️ Installation

1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   uv venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   # Install the project and its dependencies
   uv add openai-agents python-dotenv chainlit
   ```
4. Create a `.env` file with your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## 🚀 Usage

Start the application:

```bash
uv run chainlit run main.py -w
```

Then open your browser at `http://localhost:8000` and start chatting!

## 🧩 How It Works

The chatbot is built on three main components:

1. **Chainlit** - Provides the chat interface and session management
2. **Agents SDK** - Provides the agent framework for conversation handling
3. **Gemini 2.0 Flash** - The underlying language model that powers the responses

The application maintains a conversation history, allowing the AI to refer to previous exchanges and remember information like names and preferences throughout the session.

## 💻 Code Explanation

The main application logic:

- Sets up the Gemini model with OpenAI compatibility API
- Configures the agent with appropriate instructions
- Manages conversation history between messages
- Processes user input and displays AI responses

## 📝 License

MIT

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

Made with ❤️ using Chainlit and Google's Generative AI
