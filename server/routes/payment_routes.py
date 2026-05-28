from fastapi import APIRouter, Request, Response, status
from fastapi.responses import FileResponse
from config.config import WEBAPP_PATH
from logs.logger import logger
from db.payments_crud import update_payment_status
from db.users_crud import update_user_sub_status
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config.config import TELEGRAM_INVITE_LINK, NOTIFICATION_ID
from db.payments_crud import create_payment, get_payment_by_subscription_id

router = APIRouter()


@router.post("/pay/")
async def pay_confirm(request: Request):
    data = await request.form()
    logger.info(data)

    # Понять это продление подписки или нет

    invoice_id = data.get("InvoiceId")
    subscription_id = data.get("SubscriptionId")

    if invoice_id:
        payment = await update_payment_status(invoice_id, data["Status"], subscription_id)
        logger.info(
            f"Платеж обновлен: {payment.user.email} — {payment.sub_type} — {payment.invoice_id}"
        )
        await update_user_sub_status(payment.user.telegram_id, payment.sub_type)

        keyboard = [
            [InlineKeyboardButton("Присоединиться к каналу", url=TELEGRAM_INVITE_LINK)]
        ]
        markup = InlineKeyboardMarkup(keyboard)
        try:
            await request.app.state.bot_app.bot.send_message(
                payment.user.telegram_id,
                "Ваша подписка успешно активирована. Теперь ты можешь присоединиться к нашему каналу: ",
                reply_markup=markup,
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения пользователю: {e}")

        try:
            await request.app.state.bot_app.bot.send_message(
                NOTIFICATION_ID,
                "Пользователь "
                + payment.user.username
                + " ("
                + str(payment.user.telegram_id)
                + ") купил подписку "
                + payment.sub_type
                + " на сумму "
                + str(payment.amount)
                + " рублей",
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения в канал: {e}")

        return Response(status_code=status.HTTP_200_OK)
    elif subscription_id:
        # это продление подписки — значит нам нужно создать платеж 2
        first_payment = await get_payment_by_subscription_id(subscription_id)
        
        payment = await create_payment(first_payment.user.id, first_payment.sub_type, subscription_id=subscription_id)
        
        await update_user_sub_status(payment.user.telegram_id, payment.sub_type)
        
        logger.info(f"Платеж создан: {payment.user.email} — {payment.sub_type} — {payment.invoice_id}")
        
        try:
            await request.app.state.bot_app.bot.send_message(
                payment.user.telegram_id,
                "Ваша подписка успешно продлена. Чтобы её отменить сделайте ",
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения пользователю: {e}")
            
        try:
            await request.app.state.bot_app.bot.send_message(
                NOTIFICATION_ID,
                "Пользователь "
                + payment.user.username
                + " ("
                + str(payment.user.telegram_id)
                + ") продлил подписку "
                + payment.sub_type
                + " на сумму "
                + str(payment.amount)
                + " рублей",
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения в канал: {e}")
        return Response(status_code=status.HTTP_200_OK)
    


    return Response(status_code=status.HTTP_200_OK)
