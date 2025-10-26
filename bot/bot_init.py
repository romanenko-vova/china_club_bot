from telegram.ext import (
    Application,
    CommandHandler,
)
from telegram.ext import (
    ConversationHandler,
    PicklePersistence
)
from config.config import TELEGRAM_TOKEN
from bot.handlers.start_handler import start
from logs.logger import logger

def init_bot():
    persistence = PicklePersistence("bot_cache")
    application = (
        Application.builder()
        .token(TELEGRAM_TOKEN)
        .persistence(persistence)
        .build()
    )
    logger.info("Запуск тг бота ✅")
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={},
        fallbacks=[CommandHandler("start", start)],
        name="main_conversation",
        persistent=True,
    )
    application.add_handler(conv_handler)

    return application