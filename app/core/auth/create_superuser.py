import contextlib

from models import db_helper, User
from .dependencies import get_user_db, get_user_manager
from core.schemas.user_schemas import UserCreate
from fastapi_users.exceptions import UserAlreadyExists
from core.auth import UserManager
import asyncio
from os import getenv

get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    email: str,
    password: str,
    username: str,
    is_active: bool = True,
    is_superuser: bool = True,
    is_verified: bool = True):
    try:
        async with db_helper.postgres.session_maker() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await create_user(
                        user_manager,
                        UserCreate(
                            email=email,
                            password=password,
                            username=username,
                            is_superuser=is_superuser,
                            is_active=is_active,
                            is_verified=is_verified,
                        )
                    )
                    print(f"User created {user}")
                    return user
    except UserAlreadyExists:
        print(f"User {email} already exists")

email = getenv("ADMIN_DEFAULT_EMAIL", "admin@admin.ru")
password = getenv("ADMIN_DEFAULT_PASSWORD", "admin")
username = getenv("ADMIN_DEFAULT_USERNAME", "admin")

if __name__ == "__main__":
    asyncio.run(create_superuser(email, password, username))