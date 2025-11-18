from sys import base_prefix
from fastapi import FastAPI
from contextlib import asynccontextmanager
from bot.bot_init import init_bot
from config.config import WEBHOOK_URL, TELEGRAM_PATH, TELEGRAM_SECRET_TOKEN
from telegram import Update
from server import telegram_router, webapp_router


def init_fastapi():
    app = FastAPI(lifespan=lifespan)
    app.include_router(telegram_router)
    app.include_router(webapp_router)
    @app.get("/")
    async def read_root():
        return {"message": "Hello, World!"}

    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Что будет происходить при запуске сервера
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
