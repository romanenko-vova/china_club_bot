from telegram.ext import (
    Application,
    CommandHandler,
)
from telegram.ext import (
    ConversationHandler,
    PicklePersistence,
    ChatJoinRequestHandler,
    MessageHandler,
    filters,
    ChatMemberHandler,
)
from config.config import TELEGRAM_TOKEN
from bot.handlers.start_handler import start
from logs.logger import logger
from bot.handlers.join_request_handler import join_request_handler
from bot.handlers.remove_chat_join_messages_handler import (
    handle_message,
    handle_chat_member,
)
from bot.handlers.job_remove_debtors import check_sub_status


def init_bot():
    persistence = PicklePersistence("bot_cache")
    application = (
        Application.builder().token(TELEGRAM_TOKEN).persistence(persistence).build()
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
    
    application.add_handler(ChatJoinRequestHandler(join_request_handler))
    
    application.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS
            | filters.StatusUpdate.LEFT_CHAT_MEMBER,
            handle_message,
        )
    )
    application.add_handler(
        ChatMemberHandler(handle_chat_member, ChatMemberHandler.CHAT_MEMBER)
    )
    
    application.job_queue.run_once(check_sub_status, when=5)

    return application
