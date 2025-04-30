import os
from dotenv.main import load_dotenv
import telebot
import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
bot = telebot.TeleBot(
    os.getenv('api_tele')
)
conversation_history = {}

def generate_response(user_id, text):
    if user_id not in conversation_history:
        conversation_history[user_id] = []

    conversation_history[user_id].append({"role": "user", "content": text})

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-4-maverick:free",  # you can changed using other models
        "messages": conversation_history[user_id]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status() 
        
        reply = response.json()['choices'][0]['message']['content'].strip()
        conversation_history[user_id].append({"role": "assistant", "content": reply})
        return reply
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        return "Sorry, I encountered an error while processing your request. Please try again later."
    except (KeyError, IndexError) as e:
        logger.error(f"Error parsing API response: {str(e)}")
        return "Sorry, there was an error processing the response. Please try again."

# handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user_input = message.text
    response = generate_response(user_id, user_input)
    bot.reply_to(message, response)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
