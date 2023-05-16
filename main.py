from fastapi import FastAPI
from api.v1.api import Api_router
from core.config import settings


app = FastAPI(
    title='API de Cadastro de Contas.'
)

app.include_router(Api_router, prefix=settings.API_V1_STR)

# /api/v1/...


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8001, log_level='info', reload=True)
