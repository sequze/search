from fastapi_users.authentication import (
    BearerTransport,
    AuthenticationBackend,
)
from fastapi_users import FastAPIUsers
from .dependencies import get_jwt_strategy, get_user_manager
from models import User

# TODO: изменить на нормальный путь
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
