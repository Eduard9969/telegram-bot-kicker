import os

from dotenv import load_dotenv

load_dotenv()

IS_DEBUG = os.getenv('IS_DEBUG', default=False)

TELEGRAM_BOT_AUTH_TOKEN = os.getenv('TELEGRAM_BOT_AUTH_TOKEN', default=None)
TELEGRAM_INSPECTOR_CHANNEL = os.getenv('TELEGRAM_INSPECTOR_CHANNEL', default=None)