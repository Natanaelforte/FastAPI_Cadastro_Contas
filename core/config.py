from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://natanael:138904@localhost:5432/cadastro_de_contas'
    DBBaseModel = declarative_base()

    class Config:
        arbitrary_types_allowed = True
        case_sensitive = True


settings = Settings()
