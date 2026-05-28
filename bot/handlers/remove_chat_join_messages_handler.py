from telegram import Update
from telegram.ext import ContextTypes

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.chat:
        return
    message = update.message
    try:
        await message.delete()
    except Exception:
        pass


async def handle_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.chat_member or not update.message:
        return
    
    chat_member = update.chat_member
    old_status = chat_member.old_chat_member.status
    new_status = chat_member.new_chat_member.status
    
    if old_status != new_status and (new_status == "kicked" or new_status == "left"):
        try:
            await update.message.delete()
        except Exception:
            pass