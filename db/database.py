from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from db.models import Base
from contextlib import asynccontextmanager
from config.config import DATABASE_URL

# postgresql+asyncpg://<user>:<password>@<host>:<port>/<database>
engine = create_async_engine(DATABASE_URL, echo=True)

async_session_maker = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # Создавать все таблицы в базе данных