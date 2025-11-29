from sys import base_prefix
from fastapi import FastAPI
from contextlib import asynccontextmanager
from bot.bot_init import init_bot
from config.config import WEBHOOK_URL, TELEGRAM_PATH, TELEGRAM_SECRET_TOKEN
from telegram import Update
from server import telegram_router, payment_router, api_router, common_router
from db.database import init_db


def init_fastapi():
    app = FastAPI(lifespan=lifespan)
    app.include_router(common_router)
    app.include_router(telegram_router)
    app.include_router(api_router, prefix='/api')
    app.include_router(payment_router, prefix='/cp')

    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Что будет происходить при запуске сервера
    await init_db()
    bot_app = init_bot()
    app.state.bot_app = bot_app
    await bot_app.initialize()
    await bot_app.start()
    await bot_app.bot.set_webhook(
        WEBHOOK_URL + TELEGRAM_PATH,
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
        secret_token=TELEGRAM_SECRET_TOKEN,
    )
    yield
    # Что будет происходить при завершении работы сервера
    await bot_app.stop()
    await bot_app.shutdown()
    await bot_app.bot.delete_webhook()
