import os
from dotenv import load_dotenv
from telebot import TeleBot, types


load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
TELEGRAM_BOT_URL = os.environ.get("TELEGRAM_BOT_URL")
TG_MINI_APP_URL = os.environ.get("TG_MINI_APP_URL")
HELP_WEBSITE = os.environ.get("HELP_WEBSITE")

bot = TeleBot(TELEGRAM_BOT_TOKEN)