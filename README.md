<div align="center">

**English** | [🇩🇪 Deutsch](README.de.md) | [🇮🇷 فارسی](README.fa.md)

</div>

---
# 🤖 AI Chatbot in Telegram

> **Build your own AI-powered Telegram chatbot — using either a remote AI API or a local LLM with Ollama.**

A simple and beginner-friendly Python project that connects **Telegram** with an AI model.

This repository provides **two ways to run your chatbot**:

* ☁️ **API Mode** — connect Telegram to an AI API such as an OpenAI-compatible endpoint.
* 🖥️ **Local Mode** — run an AI model locally with **Ollama**, without sending your conversations to a remote AI API.

The project is designed to be easy to understand, customize, and extend.

---

## ✨ Features

* 🤖 AI-powered conversations directly inside Telegram
* 💬 Simple text-based chat interface
* ⚡ Asynchronous Telegram message handling
* ☁️ Support for remote AI APIs
* 🖥️ Support for locally hosted AI models with Ollama
* 🔐 API key and Telegram bot token configuration
* 🧩 Easy-to-customize Python source code
* ⏳ Processing/status messages while generating responses
* 🛠️ Beginner-friendly implementation

---

## 🏗️ How It Works

The project follows a simple flow:

```text
                 Telegram
                    │
                    ▼
             ┌──────────────┐
             │  Telegram Bot │
             └───────┬──────┘
                     │
              User sends message
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   ☁️ API MODE              🖥️ LOCAL MODE
          │                     │
          ▼                     ▼
   Remote AI API              Ollama
          │                     │
          └──────────┬──────────┘
                     ▼
              AI-generated reply
                     │
                     ▼
                 Telegram
```

---

# 📁 Project Structure

```text
Ai-chatbot-in-telegram/
│
├── chatbot(api).py       # ☁️ API-based AI chatbot
├── chatbot(local).py     # 🖥️ Local Ollama chatbot
├── .gitignore
└── README.md
```

The repository intentionally keeps the implementations small so you can easily understand how Telegram and AI APIs communicate.

---

# ☁️ Option 1 — API-Based Chatbot

The API version uses:

* Python
* `python-telegram-bot`
* `httpx`
* An OpenAI-compatible AI API

The current implementation sends the user's message to a configurable API endpoint and extracts the assistant response from the API's `choices` response structure.

### Architecture

```text
Telegram
   │
   ▼
Python Telegram Bot
   │
   ▼
HTTP Request
   │
   ▼
AI API
   │
   ▼
AI Response
   │
   ▼
Telegram
```

### 1. Install dependencies

```bash
pip install python-telegram-bot httpx
```

### 2. Configure the bot

Open:

```text
chatbot(api).py
```

Configure these values:

```python
API_URL = "YOUR_API_URL"
API_KEY = "YOUR_API_KEY"
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
MODEL_NAME = "YOUR_MODEL_NAME"
```

> ⚠️ **Never commit real API keys or bot tokens to GitHub.**

### 3. Run the bot

Because the filename contains parentheses, run it like this:

```bash
python "chatbot(api).py"
```

You should see:

```text
🤖 Telegram bot is running and connected to ArvanCloud AI...
```

Then open your Telegram bot and send a message.

---

# 🖥️ Option 2 — Local AI with Ollama

Want to run the AI **locally**?

The repository also includes an Ollama implementation.

This version communicates with an AI model running on your own machine instead of sending the prompt to a remote AI API.

### Architecture

```text
Telegram
   │
   ▼
Python Telegram Bot
   │
   ▼
Ollama
   │
   ▼
Local AI Model
   │
   ▼
AI Response
   │
   ▼
Telegram
```

### 1. Install Ollama

Install Ollama for your operating system, then verify it:

```bash
ollama --version
```

Check your installed models:

```bash
ollama list
```

### 2. Pull an AI model

For example:

```bash
ollama pull llama3.2
```

You can use another model supported by your Ollama installation.

### 3. Install Python dependencies

```bash
pip install python-telegram-bot ollama
```

### 4. Configure the model

Open:

```text
chatbot(local).py
```

Find:

```python
model='youre_local_Ai_name'
```

and replace it with your installed Ollama model:

```python
model='llama3.2'
```

Also replace:

```python
"YOUR_BOT_TOKEN"
```

with your Telegram bot token.

### 5. Run the bot

```bash
python "chatbot(local).py"
```

Then open Telegram and start chatting.

---

# 🤖 Creating Your Telegram Bot

You need a Telegram bot token before running either version.

### Step 1 — Open BotFather

In Telegram, search for:

```text
@BotFather
```

### Step 2 — Create a bot

Send:

```text
/newbot
```

Follow the instructions and choose:

* A display name
* A unique username ending in `bot`

BotFather will provide a token similar to:

```text
123456789:ABCxxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 3 — Add the token to your project

Use the token in the appropriate Python file.

**Do not publish the token publicly.**

If a token is accidentally exposed, revoke it and generate a new one through BotFather.

---

# 💬 Using the Bot

Once your bot is running:

### Start the bot

```text
/start
```

The bot will respond that it is ready.

### Send a message

```text
Hello!
```

The bot will process the message and return the AI-generated response.

Example:

```text
You:
Explain Python decorators in simple terms.

Bot:
A decorator is a function that modifies or extends
the behavior of another function...
```

---

# ⚙️ Customization

This project is intentionally simple, which makes it easy to modify.

You can customize:

### 🧠 AI model

Change the model used by your API or Ollama.

### 🌡️ Temperature

The API implementation currently uses:

```python
"temperature": 0.7
```

The local implementation uses:

```python
'temperature': 0.1
```

A higher temperature generally produces more varied responses, while a lower value tends to produce more deterministic responses.

### 📏 Maximum response length

The API implementation uses:

```python
"max_tokens": 512
```

The Ollama implementation uses:

```python
'num_predict': 512
```

Adjust these values depending on the model and use case.

---

# 🔐 Security

**Never hard-code secrets in a public repository.**

Avoid committing:

```python
API_KEY = "real-secret-key"
BOT_TOKEN = "real-telegram-token"
```

Instead, use environment variables.

For example:

```bash
export TELEGRAM_BOT_TOKEN="your-token"
export AI_API_KEY="your-api-key"
```

Then in Python:

```python
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("AI_API_KEY")
```

A `.env` file can also be used with `python-dotenv`.

Example:

```env
TELEGRAM_BOT_TOKEN=your_telegram_token
AI_API_KEY=your_api_key
```

And make sure `.env` is included in `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
```

---

# 🛠️ Troubleshooting

## Bot does not start

Check that your Telegram bot token is correct.

```text
YOUR_BOT_TOKEN
```

must be replaced with the real token.

---

## API mode returns an error

Check:

* API URL
* API key
* Model name
* Internet connection
* API compatibility
* API response format

The API implementation already handles common timeout and HTTP errors.

---

## Ollama mode does not work

First check Ollama:

```bash
ollama list
```

Then make sure the model configured in `chatbot(local).py` exists.

For example:

```python
model='llama3.2'
```

If necessary:

```bash
ollama pull llama3.2
```

---

## Bot responds slowly

For local models, response speed depends on:

* CPU
* GPU
* RAM
* Model size
* Ollama configuration

For API mode, performance depends mainly on your network connection and the selected AI provider/model.

---

# 🚀 Ideas for Future Improvements

This project provides a simple foundation. Some useful next steps would be:

* 🧠 Conversation memory
* 👤 Per-user conversation history
* 🔄 `/reset` command
* 🎙️ Voice message support
* 🖼️ Image understanding
* 🎨 AI image generation
* 📎 File/document processing
* 🌍 Multi-language support
* 👥 Group chat support
* 🔐 User authorization
* ⚙️ Configuration through environment variables
* 📝 Better logging
* 🐳 Docker support
* ☁️ Deployment to a VPS/cloud server
* 🔌 Support for multiple AI providers
* 📊 Usage and token tracking

---

# 🧪 Development

Clone the repository:

```bash
git clone https://github.com/kasranaqhdpur/Ai-chatbot-in-telegram.git
```

Enter the project:

```bash
cd Ai-chatbot-in-telegram
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install python-telegram-bot httpx ollama
```

Choose either API mode or local mode and configure the required credentials/model.

---

# 🤝 Contributing

Contributions are welcome! 🎉

If you have an idea that could improve the project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/my-new-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add my new feature"
```

5. Push the branch

```bash
git push origin feature/my-new-feature
```

6. Open a Pull Request

Bug reports, feature requests, documentation improvements, and code contributions are all welcome.

---

# ⭐ Support the Project

If this project helped you learn something new or build your own Telegram AI bot:

**⭐ Star the repository on GitHub!**

It helps the project reach more developers.

---

# 📜 License

This project does not currently include a license file in the repository.

If you intend to make the project open-source for others to reuse, consider adding a license such as **MIT**.

---

# 👨‍💻 Author

Created by **kasranaqhdpur**.

Repository:

https://github.com/kasranaqhdpur/Ai-chatbot-in-telegram

---

## 💡 Why This Project?

Building an AI chatbot doesn't have to be complicated.

This project demonstrates the core idea:

```text
Telegram
   +
Python
   +
AI
   =
🤖 Your Own Telegram AI Assistant
```

Whether you want to connect to a cloud AI API or run an LLM completely locally with Ollama, this repository gives you a simple starting point.

**Build it. Customize it. Make it yours. 🚀**
