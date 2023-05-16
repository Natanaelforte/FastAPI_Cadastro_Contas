from fastapi import FastAPI
from core.config import settings
from api.v1 import api


app = FastAPI(
    title='API de Cadastro de Contas.'
)

app.include_router(api.Api_router, prefix=settings.API_V1_STR)

# /api/v1/...


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8001, log_level='info')
