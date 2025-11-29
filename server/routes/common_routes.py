from fastapi import APIRouter, Response, status


router = APIRouter()

@router.get("/")
async def read_root():
    return Response(status_code=status.HTTP_200_OK, content="Hello, World!")