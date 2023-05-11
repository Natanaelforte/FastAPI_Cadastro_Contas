from typing import list
from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://natanael:130489@localhost:5432/cadastro_de_contas'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True
