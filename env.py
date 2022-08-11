import os

IS_DEBUG = os.getenv('IS_DEBUG', default=False)

TELEGRAM_BOT_AUTH_TOKEN = os.getenv('TELEGRAM_BOT_AUTH_TOKEN', default=None)
TELEGRAM_INSPECTOR_CHANNEL = os.getenv('TELEGRAM_INSPECTOR_CHANNEL', default=None)

TELEGRAM_APP_CLIENT_ID = os.getenv('TELEGRAM_BOT_APP_CLIENT_ID', default=None)
TELEGRAM_APP_API_HASH = os.getenv('TELEGRAM_BOT_APP_API_HASH', default=None)