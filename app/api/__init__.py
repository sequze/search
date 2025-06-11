from .search.routes import router as search_router
from .auth.routes import router as auth_router, user_router as user_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(auth_router, prefix="/auth")
router.include_router(search_router, prefix="/search")
router.include_router(user_router, prefix="/users")

__all__ = [
    "router",
]
