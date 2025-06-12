from typing import TYPE_CHECKING
from fastapi import Depends
from .user_manager import UserManager
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users.authentication import JWTStrategy
from models import User, db_helper
from config import settings
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(session: AsyncSession = Depends(db_helper.postgres.session_getter)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.auth_config.private_key_path.read_text(),
        public_key=settings.auth_config.public_key_path.read_text(),
        lifetime_seconds=3600,
        algorithm="RS256",
        )
