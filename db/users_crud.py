from db.database import get_db_session
from db.models import User
from sqlalchemy import select

async def create_user(telegram_id: int, username:str = None):
    async with get_db_session() as session:
        user = User(telegram_id=telegram_id)
        if username:
            user.username = username
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
        
async def get_user_by_telegram_id(telegram_id: int):
    async with get_db_session() as session:
        cursor = await session.execute(select(User).where(User.telegram_id == telegram_id))
        return cursor.scalar_one_or_none()
    
async def update_user_username(telegram_id: int, username: str):
    async with get_db_session() as session:
        cursor = await session.execute(select(User).where(User.telegram_id == telegram_id))
        user = cursor.scalar_one_or_none()
        if user:
            user.username = username
            await session.commit()
            return user
        return None
    
async def update_user_email(telegram_id: int, email: str):
    async with get_db_session() as session:
        cursor = await session.execute(select(User).where(User.telegram_id == telegram_id))
        user = cursor.scalar_one_or_none()
        if user:
            user.email = email
            await session.commit()
            return user
        return None

async def delete_user(telegram_id: int):
    async with get_db_session() as session:
        user = await get_user_by_telegram_id(telegram_id)
        if user:
            await session.delete(user)
            await session.commit()
            return True
        return False