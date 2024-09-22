import os

from fastapi import FastAPI
import uvicorn

from bootstrap import get_container
from routes import sales_router

app = FastAPI(
    openapi_tags=[],
    title="Trabalho 2 - API REST com FastAPI",
    description="API REST para manipulação do dataset de vendas com operações GET, POST, PUT e DELETE.",
    version="1.0.0",
)

app.state.ioc_container = get_container()

app.include_router(sales_router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
