import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8081015750:AAFO5Kz4tzjUMsszMP1nyUnAHR8lHIirqgM")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот Burger King. Напиши ключевое слово, и я пришлю нужную презентацию.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    # Пример простой логики
    if "маркетинг" in text:
        await update.message.reply_text("Вот презентация по маркетингу: [ссылка]")
    elif "финансы" in text:
        await update.message.reply_text("Вот презентация по финансам: [ссылка]")
    else:
        await update.message.reply_text("Извините, я не нашёл презентацию по этому слову.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
import json

with open('data.json', 'r', encoding='utf-8') as f:
    database = json.load(f)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    query = message.text.lower()
    response = database.get(query, "Извините, ничего не найдено.")
    bot.send_message(message.chat.id, response)


