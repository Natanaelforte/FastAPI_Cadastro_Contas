from typing import Optional
from pydantic import BaseModel as SCBaseModel


class contas_response(SCBaseModel):
    id = Optional[int]
    descricao = str
    valor = float
    status = str

    class Config:
        orm_mode = True


class contas_request(SCBaseModel):
    id = Optional[int]
    descricao = str
    valor = float
    status = str

    class Config:
        orm_mode = True
