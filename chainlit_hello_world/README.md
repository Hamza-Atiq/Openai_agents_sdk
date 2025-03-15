# Chainlit Hello World

A simple chatbot demo built with Chainlit that echoes back user messages.

## Overview

This project is a minimal example of a chatbot created using Chainlit. When a user sends a message, the bot responds by greeting the user with "Hello" followed by the user's message.

## Project Structure

- `chatbot.py` - The main application file containing the chatbot logic
- `.chainlit/` - Directory containing Chainlit configuration and translations
- `chainlit.md` - Markdown file for the homepage of your Chainlit app

## Prerequisites

- Python 3.11 or higher
- UV package manager (recommended)

## Setup

1. Create a virtual environment:

```bash
uv venv
```

2. Activate the virtual environment:

```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. Install the required packages:

```bash
uv add chainlit
```

## Running the Application

You can run the application using the following command:

```bash
uv run chainlit run chatbot.py
```

To run with auto-reload on file changes (development mode):

```bash
uv run chainlit run chatbot.py -w
```

The application will be available at http://localhost:8000

## How It Works

The chatbot uses Chainlit's `@cl.on_message` decorator to handle incoming messages:

```python
import chainlit as cl

@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content=f"Hello {message.content}").send()
```

This simple handler receives the user's message and responds with "Hello" followed by the user's message content.

## Customization

You can customize the app's appearance and behavior by modifying:
- `.chainlit/config.toml` - For app configuration
- `chainlit.md` - For the welcome screen content

## License

[MIT](https://choosealicense.com/licenses/mit/)
