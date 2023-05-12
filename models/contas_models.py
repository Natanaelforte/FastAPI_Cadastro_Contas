from core.config import settings
from sqlalchemy import Column, Integer, String, Float



class contas_model(settings.DBBaseModel):
    __tablename__ = 'contas'
    __allow_unmapped__ = True

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    descricao: str = Column(String(150))
    valor: float = Column(Float)
    status: str = Column(String(150))  # pago ou não pago



