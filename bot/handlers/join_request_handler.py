from telegram import Update
from telegram.ext import ContextTypes
from db.users_crud import get_user_by_telegram_id
from logs.logger import logger

async def join_request_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user = await get_user_by_telegram_id(update.effective_user.id)
    if not user:
        return
    
    if user.sub_status == 'active':
        await context.bot.approve_chat_join_request(update.effective_chat.id, update.effective_user.id)
