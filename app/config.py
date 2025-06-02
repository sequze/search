from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

postgres_url = os.getenv("postgres_url")
mysql_url = os.getenv("mysql_url")
mongo_url = os.getenv("mongodb_url")


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class DatabaseConfig(BaseModel):
    url: str
    echo: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings:
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    postgres_config = DatabaseConfig(url=postgres_url)
    mysql_config = DatabaseConfig(url=mysql_url)
    mongodb_config = mongo_url
    run = RunConfig()


settings = Settings()
