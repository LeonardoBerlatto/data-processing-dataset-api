from fastapi import FastAPI

from bootstrap import get_container
from routes import sales_router

app = FastAPI(
    openapi_tags=[],
    title="Trabalho 2 - API REST com FastAPI",
    description="API REST para manipulação do dataset de vendas com operações GET, POST, PATCH e DELETE.",
    version="1.0.0",
)

app.state.ioc_container = get_container()

app.include_router(sales_router)
