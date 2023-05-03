from fastapi import FastAPI
from router import contas_router


app = FastAPI(
    title='API de Cadastro de Contas.'
)

app.include_router(contas_router.router, tags=['contas'])







if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8001)
