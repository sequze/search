from sqlalchemy.orm import Mapped
from fastapi_users.db import SQLAlchemyBaseUserTable
from .base import Base


class User(Base, SQLAlchemyBaseUserTable[int]):
    username: Mapped[str]
