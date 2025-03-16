# 🤖 Customized Tools with OpenAI SDK

![OpenAI](https://img.shields.io/badge/OpenAI-API-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Chainlit](https://img.shields.io/badge/Chainlit-latest-orange)

A powerful chatbot application leveraging the OpenAI SDK to provide customized tools functionality in a conversational interface.

## ✨ Features

- **Weather Information**: Get current weather conditions for specific cities
- **Date & Time**: Check current date and time information
- **Student Records**: Query student information using roll numbers
- **Conversation History**: Maintains context throughout the conversation
- **Web Interface**: Clean and responsive UI powered by Chainlit

## 🛠️ Technology Stack

- **Gemini API**: For powerful LLM capabilities
- **Chainlit**: For creating the conversational interface
- **UV Package Manager**: For efficient Python package management
- **Python 3.9+**: Core programming language

## 📋 Prerequisites

- Python 3.9 or later
- UV package manager
- Gemini API key

## 🚀 Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/openai_agents_sdk.git
cd openai_agents_sdk/customized_tools
```

2. Set up a virtual environment:
```bash
uv venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies using UV:
```bash
uv add openai-agents python-dotenv chainlit
```

### Configuration

Create a `.env` file in the project root with your API keys:
```
GOOGLE_API_KEY=your_google_api_key  # If using Google's Generative Language API
```

## 🖥️ Usage

Run the application using Chainlit:
```bash
uv run chainlit run tools_with_chainlit.py -w
```

The `-w` flag enables hot-reloading for development.

Access the web interface at: http://localhost:8000

Run the tools application without Chainlit:
```bash
uv run tools_main.py
```

## 💬 Example Interactions

- "What is the temperature today in [city]?"
- "What is today's date?"
- "What is the current time?"
- "What is the name of the student with roll number [number]?"

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
