from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse
from db.users_crud import update_user_email

from logs.logger import logger
from config.config import CP_PUBLIC_ID
from uuid import uuid4

router = APIRouter()

@router.post('/order/create')
async def pay_confirm(request: Request):
    data = await request.json()
    user = await update_user_email(data['telegram_id'], data['email'])
    print(user.email)
    logger.info(data)
    invoice_id = str(uuid4())
    return JSONResponse({"public_id": CP_PUBLIC_ID, "invoice_id": invoice_id})