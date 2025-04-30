# Telegram Bot with OpenRouter AI

This repository contains a Python script that implements a Telegram bot using various AI models through OpenRouter. The bot can respond to user messages with generated responses from different AI models.

## Features

- Uses OpenRouter to access various AI models (currently using Llama maverik 4 free)
- Maintains conversation history for each user
- Responds to incoming messages on Telegram
- Robust error handling and logging

## Requirements

- Python 3.6 or higher
- `python-telegram-bot`
- `requests`
- `python-dotenv`

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/khmuhtad1n/TeleGpt.git
cd TeleGpt
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File

Create a `.env` file in the root directory of your project and add your OpenRouter API key and Telegram bot token:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
api_tele=your_telegram_bot_token
```

### 4. Running the Bot

Run the bot using the following command:

```bash
python main.py
```

## Model Configuration

The bot is currently configured to use the Llama maverick 4 (free). You can change the model by modifying the `model` parameter in the `generate_response` function in `main.py`. Available models include:

- `openai/gpt`
- `anthropic/claude`
- And many others available on OpenRouter

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License.
