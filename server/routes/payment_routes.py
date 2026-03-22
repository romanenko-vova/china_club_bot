from fastapi import APIRouter, Request, Response, status
from fastapi.responses import FileResponse
from config.config import WEBAPP_PATH
from logs.logger import logger
from db.payments_crud import update_payment_status


router = APIRouter()

@router.post('/pay')
async def pay_confirm(request: Request):
    data = await request.form()
    logger.info(data)
    payment = await update_payment_status(data['InvoiceId'], data['Status'])
    logger.info(f"Платеж обновлен: {payment.user.email} — {payment.sub_type} — {payment.invoice_id}")
    await request.app.state.bot_app.bot.send_message(payment.user.telegram_id, "Ваша подписка успешно активирована")
    return Response(status_code=status.HTTP_200_OK)