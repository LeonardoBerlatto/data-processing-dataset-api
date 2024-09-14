from fastapi import APIRouter, Query, Response

from bootstrap import resolve
from domain import Sale
from service.sale_service import SalesService

sales_router = APIRouter(prefix='/sales', tags=['Sales'])


@sales_router.get("/", summary="Buscar vendas", description="Retorna uma lista de vendas")
async def get_sales(page_number: int = Query(1, ge=0, description="Index da paginação"),
                    page_size: int = Query(10, ge=1, description="Tamanho da página"),
                    service: SalesService = resolve(SalesService)) -> list[Sale]:
    return service.get_sales(page_number, page_size)


@sales_router.get("/{invoice_id}",
                  summary="Buscar uma venda pelo `invoice_id`",
                  description="Retorna uma venda específica")
async def get_sale(invoice_id: str, service: SalesService = resolve(SalesService)) -> Sale:
    return service.get_sale(invoice_id)


@sales_router.post("/",
                   summary="Criar uma venda",
                   description="Cria uma nova venda no dataset")
async def create_sale(sale: Sale, response: Response, service: SalesService = resolve(SalesService)) -> Sale:
    new_sale = service.create_sale(sale)

    response.status_code = 201
    response.headers['Location'] = f"/sales/{new_sale.invoice_id}"
    return new_sale


@sales_router.put("/{invoice_id}",
                  summary="Atualizar uma venda",
                  description="Atualiza uma venda do dataset")
async def update_sale(invoice_id: str, sale: Sale, service: SalesService = resolve(SalesService)) -> Sale:
    return service.update_sale(invoice_id, sale)


@sales_router.delete("/{invoice_id}",
                     summary="Delete uma venda",
                     description="Deleta uma venda do dataset")
async def delete_sale(invoice_id: str, response: Response, service: SalesService = resolve(SalesService)):
    service.delete_sale(invoice_id)

    response.status_code = 204
    return response
