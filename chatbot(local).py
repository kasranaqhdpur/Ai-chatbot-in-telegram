import ollama
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

def query_ollama(question: str) -> str:
    try:
        response = ollama.chat(
            model='youre_local_Ai_name ',
            messages=[{'role': 'user', 'content': question}],
            options={
                'temperature': 0.1,
                'top_p': 0.9,
                'num_predict': 512, 
                'timeout': 60  
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"❌ error : {str(e)} - check ollama list for more info"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('i am ready ... 👤')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    await update.message.reply_text('⏳processing ...')
    
    answer = query_ollama(user_text)
    await update.message.reply_text(answer)

if __name__ == '__main__': 
    
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖start ")
    app.run_polling()