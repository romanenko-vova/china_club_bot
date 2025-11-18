from fastapi import APIRouter, Request, Response, status
from fastapi.responses import FileResponse
from config.config import WEBAPP_PATH
from logs.logger import logger


router = APIRouter()

@router.get(WEBAPP_PATH)
async def webapp(request: Request):
    return FileResponse("./templates/index.html")