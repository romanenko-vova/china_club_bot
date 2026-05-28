from db.database import get_db_session
from db.models import User
from sqlalchemy import select
from datetime import datetime, timedelta
from config.prices import prices

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
    
async def update_user_sub_status(telegram_id: int, sub_type: str):
    async with get_db_session() as session:
        cursor = await session.execute(select(User).where(User.telegram_id == telegram_id))
        user = cursor.scalar_one_or_none()
        if user:
            user.sub_status = 'active'
            user.sub_end_date = datetime.now() + timedelta(days=prices[sub_type]['days'])
            user.sub_ban_date = user.sub_end_date + timedelta(days=2)
            await session.commit()
            return user
        return None
    
async def get_users_with_expired_sub():
    async with get_db_session() as session:
        cursor = await session.execute(select(User).where(User.sub_status == 'active', User.sub_ban_date < datetime.now()))
        return cursor.scalars().all()
    
async def update_users_in_db(kicked_users: list[int]):
    async with get_db_session() as session:
        for telegram_id in kicked_users:
            user = await get_user_by_telegram_id(telegram_id)
            if user:
                user.sub_status = 'expired'
                await session.commit()
        return True