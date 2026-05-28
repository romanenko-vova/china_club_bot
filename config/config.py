import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
TELEGRAM_PATH = os.getenv("TELEGRAM_PATH")
TELEGRAM_SECRET_TOKEN = os.getenv("TELEGRAM_SECRET_TOKEN")

WEBAPP_PATH = os.getenv("WEBAPP_PATH")

CP_PUBLIC_ID = os.getenv("CP_PUBLIC_ID")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///database.db")

TELEGRAM_INVITE_LINK = os.getenv("TELEGRAM_INVITE_LINK")

NOTIFICATION_ID = os.getenv("NOTIFICATION_ID")

CHANNEL_ID = os.getenv("CHANNEL_ID")