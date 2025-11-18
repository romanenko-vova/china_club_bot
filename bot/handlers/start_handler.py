from telegram import (
    Update,
    WebAppInfo,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes
from config.config import WEBHOOK_URL, WEBAPP_PATH


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [
        [
            InlineKeyboardButton(
                "Открыть веб-приложение",
                web_app=WebAppInfo(url=WEBHOOK_URL + WEBAPP_PATH),
            )
        ]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! Я бот для управления вашим ботом.",
        reply_markup=markup,
    )
