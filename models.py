from typing import Optional
from pydantic import BaseModel


class contas_response(BaseModel):
    id = int
    descricao = str
    valor = float
    status = str  # pago ou não pago


class contas_request(BaseModel):
    descricao = str
    valor = float
    status = str
