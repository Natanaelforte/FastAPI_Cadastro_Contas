from typing import Optional
from pydantic import BaseModel as SCBaseModel


class contas_schema(SCBaseModel):
    id: Optional[int] = int
    descricao: str = str
    valor: float = float
    status: str = str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True



