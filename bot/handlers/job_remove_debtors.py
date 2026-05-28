from telegram.ext import ContextTypes
from db.users_crud import get_users_with_expired_sub
from config.config import CHANNEL_ID
from logs.logger import logger
from db.users_crud import update_users_in_db

async def check_sub_status(context: ContextTypes.DEFAULT_TYPE):
    users = await get_users_with_expired_sub()
    kicked_users = []
    for user in users:
        try:
            await context.bot.ban_chat_member(CHANNEL_ID, user.telegram_id)
            logger.info(f"Пользователь {user.telegram_id} выкинут из канала {CHANNEL_ID}")
            await context.bot.unban_chat_member(CHANNEL_ID, user.telegram_id)
            kicked_users.append(user.telegram_id)
        except Exception as e:
            logger.error(f"Ошибка при выкидывании пользователя {user.telegram_id}: {e}")
            
        try:
            await context.bot.send_message(user.telegram_id, "Ваша подписка закончилась. Пожалуйста, купите новую подписку.")
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения пользователю {user.telegram_id}: {e}")
            
    await update_users_in_db(kicked_users)