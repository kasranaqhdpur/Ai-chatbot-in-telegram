import httpx
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

API_URL = "website_URL"
API_KEY = "api_key"
BOT_TOKEN = "bot_token",
API_TIMEOUT = 60
MODEL_NAME = "name_of_your_model"

async def query_api(question: str) -> str:
    """
    Send the user's question to the ArvanCloud AI endpoint
    and return the assistant's reply.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": question}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }

    try:
        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            response = await client.post(API_URL, json=payload, headers=headers)
            response.raise_for_status()

            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                message = data["choices"][0].get("message", {})
                content = message.get("content", "").strip()
                if content:
                    return content
                else:
                    return "⚠️ The API returned an empty response."
            else:
                return f"⚠️ Unexpected API response structure: {data}"

    except httpx.TimeoutException:
        return "❌ The API took too long to respond. Please try again later."
    except httpx.HTTPStatusError as e:
        return f"❌ API error (HTTP {e.response.status_code}): {e.response.text}"
    except Exception as e:
        return f"❌ An unexpected error occurred: {str(e)}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🤖 I am ready! Send me a message and I'll forward it to the ArvanCloud AI."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    await update.message.reply_text("⏳ Processing your request...")

    answer = await query_api(user_text)
    await update.message.reply_text(answer)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Telegram bot is running and connected to ArvanCloud AI...")
    app.run_polling()