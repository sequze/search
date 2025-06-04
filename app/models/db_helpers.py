from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy import select
from config import DatabaseConfig
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie
from .request import Request


class DatabaseHelper:
    def __init__(self, config: DatabaseConfig):
        self.engine = create_async_engine(
            url=config.url,
            echo=config.echo,
            pool_size=config.pool_size,
            max_overflow=config.max_overflow,
        )

        self.session_maker = async_sessionmaker(
            self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self):
        async with self.session_maker() as session:
            yield session


# MongoDb

class RequestMongoModel(Document):
    name: str

    class Settings:
        name = "requests"


class MongoDbHelper:
    def __init__(self, config: str):
        self.client = AsyncIOMotorClient(config)

    async def init_db(self):
        await init_beanie(
            self.client["search"],
            document_models=[RequestMongoModel]
            )

    async def search(request: str):
        pass

    async def add_request(self, request: Request):
        req = RequestMongoModel(name=request.name)
        await req.save()

    async def dispose(self):
        await self.client.close()


# General Database class
class DatabaseWorker:
    def __init__(
        self, postgres: DatabaseConfig,
        mysql: DatabaseConfig,
        mongodb_url: str
    ):
        self.postgres = DatabaseHelper(postgres)
        self.mysql = DatabaseHelper(mysql)
        self.mongodb = MongoDbHelper(mongodb_url)

    async def dispose_all(self):
        await self.postgres.dispose()
        await self.mysql.dispose()
        await self.mongodb.dispose()


    async def init(self):
        await self.mongodb.init_db()


db_helper = DatabaseWorker(
    postgres=settings.postgres_config,
    mongodb_url=settings.mongodb_config,
    mysql=settings.mysql_config)
