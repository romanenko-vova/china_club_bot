from fastapi import APIRouter, Request, Response, status
from fastapi.responses import FileResponse
from config.config import WEBAPP_PATH
from logs.logger import logger


router = APIRouter()

@router.post('/pay')
async def pay_confirm(request: Request):
    data = await request.form()
    logger.info(data)
    return Response(status_code=status.HTTP_200_OK)