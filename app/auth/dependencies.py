from typing import TYPE_CHECKING
from fastapi import Depends
from .user_manager import UserManager
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from app.models import User
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(session: "AsyncSession"):
    return SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
