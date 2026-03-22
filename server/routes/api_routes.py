from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse
from db.users_crud import update_user_email
from db.payments_crud import create_payment
from config.prices import prices

from logs.logger import logger
from config.config import CP_PUBLIC_ID
from uuid import uuid4

router = APIRouter()


@router.post("/order/create")
async def pay_confirm(request: Request):
    data = await request.json()
    user = await update_user_email(data["telegram_id"], data["email"])
    invoice_id = str(uuid4())
    sub_type = data["sub_type"]
    payment = await create_payment(user.id, sub_type, invoice_id)
    logger.info(
        f"Платеж создан: {payment.user.email} — {payment.sub_type} — {payment.invoice_id}"
    )
    return JSONResponse(
        {
            "public_id": CP_PUBLIC_ID,
            "invoice_id": payment.invoice_id,
            "amount": payment.amount,
            "description": payment.description,
            "period": prices[sub_type]["period"],
        }
    )
