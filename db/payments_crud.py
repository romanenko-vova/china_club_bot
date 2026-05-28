from db.database import get_db_session
from db.models import Payment
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from config.prices import prices


async def create_payment(user_id: int, sub_type: str, invoice_id: str = None, subscription_id: str = None):
    async with get_db_session() as session:
        if sub_type not in prices:
            raise ValueError(f"Неизвестный тип подписки: {sub_type}")
        payment = Payment(
            user_id=user_id,
            sub_type=sub_type,
            invoice_id=invoice_id,
            subscription_id=subscription_id,
            amount=prices[sub_type]["amount"],
            description=prices[sub_type]["description"],
        )
        session.add(payment)
        await session.commit()
        await session.refresh(payment)

        stmt = (
            select(Payment)
            .options(selectinload(Payment.user))
            .where(Payment.id == payment.id)
        )
        result = await session.execute(stmt)
        return result.scalars().first()


async def update_payment_status(invoice_id: str, status: str, subscription_id: str = None):
    async with get_db_session() as session:
        stmt = (
            select(Payment)
            .options(selectinload(Payment.user))
            .where(Payment.invoice_id == invoice_id)
        )
        result = await session.execute(stmt)
        payment = result.scalars().first()
        if not payment:
            raise ValueError(f"Платеж с invoice_id {invoice_id} не найден")
        payment.status = status
        if subscription_id:
            payment.subscription_id = subscription_id
        await session.commit()
        await session.refresh(payment)
        return payment

async def get_payment_by_subscription_id(subscription_id: str):
    async with get_db_session() as session:
        stmt = (
            select(Payment)
            .options(selectinload(Payment.user))
            .where(Payment.subscription_id == subscription_id and Payment.invoice_id is not None)
        )
        result = await session.execute(stmt)
        return result.scalars().first()