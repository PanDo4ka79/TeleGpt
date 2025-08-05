import telebot
import requests
import os
import traceback
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://yourdomain.com",  # можно изменить
            "X-Title": "TelegramBot"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.text}
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            print("⚠️ Ошибка от OpenRouter:", response.status_code, response.text)
            bot.reply_to(message, "Ошибка при подключении к OpenRouter.")
            return

        reply = response.json()["choices"][0]["message"]["content"]
        bot.reply_to(message, reply)

    except Exception as e:
        print("❌ Ошибка в коде бота:")
        traceback.print_exc()
        bot.reply_to(message, "Sorry, I encountered an error while processing your request. Please try again later.")

print("✅ Бот запущен")
bot.polling()
