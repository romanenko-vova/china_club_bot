from telegram import (
    Update,
    WebAppInfo,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes
from config.config import WEBHOOK_URL, WEBAPP_PATH
from db.users_crud import create_user, get_user_by_telegram_id, update_user_username, delete_user
from logs.logger import logger


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = await get_user_by_telegram_id(update.effective_user.id)
    if not user:
        user = await create_user(update.effective_user.id, update.effective_user.username)
    logger.info(f"Пользователь {user.id} ({user.username}) ({user.telegram_id}) ({user.created_at}) начал диалог")
    # await update_user_username(update.effective_user.id, 'биба')
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
