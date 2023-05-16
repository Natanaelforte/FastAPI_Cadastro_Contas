from fastapi import APIRouter

from api.v1.endpoints import conta


Api_router = APIRouter()
Api_router.include_router(conta.router, prefix='/contas', tags=["contas"])
