from fastapi import APIRouter
from core.auth import fastapi_users, auth_backend
from core.schemas.user_schemas import UserRead, UserCreate, UserUpdate

router = APIRouter(tags=["Auth"])
user_router = APIRouter(tags=["Users"])
user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Users"],
)
# /login
# /logout
router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/jwt",
)

# /register
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

# /verify
router.include_router(
    fastapi_users.get_verify_router(UserRead),
)


router.include_router(
    fastapi_users.get_reset_password_router(),
)
