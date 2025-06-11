from fastapi_users.authentication import (
    BearerTransport,
    JWTStrategy,
    AuthenticationBackend,
)

from config import settings
# TODO: изменить на нормальный путь
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.auth_config.private_key_path.read_text(),
        public_key=settings.auth_config.public_key_path.read_text(),
        lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
