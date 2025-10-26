from fastapi import APIRouter, Request, Response, status
from config.config import TELEGRAM_PATH, TELEGRAM_SECRET_TOKEN
from logs.logger import logger
from telegram import Update

router = APIRouter()


@router.post(TELEGRAM_PATH)
async def webhook(request: Request):
    if TELEGRAM_SECRET_TOKEN:
        header_token = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if header_token != TELEGRAM_SECRET_TOKEN:
            logger.warning("Forbidden: invalid secret token header")
            return Response(status_code=status.HTTP_403_FORBIDDEN)

    try:
        payload = await request.json()
    except Exception:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    update = Update.de_json(payload, request.app.state.bot_app.bot)
    
    await request.app.state.bot_app.update_queue.put(update)
    return Response(status_code=status.HTTP_200_OK)