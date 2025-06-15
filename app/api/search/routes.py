from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from models import db_helper, User
from core.search import search
from core.auth.helpers import current_verified_user
from fastapi import Depends

router = APIRouter(tags=["Search"])

@router.get("/request")
async def index(
    request: str,
    page: int = 1,
    size: int = 5,
    current_user: User = Depends(current_verified_user),
    postgres: AsyncSession = Depends(db_helper.postgres.session_getter),
    mysql: AsyncSession = Depends(db_helper.mysql.session_getter),
):
    return await search(
        page=page,
        size=size,
        request=request,
        limit=5,
        postgres_session=postgres,
        mysql_session=mysql,
    )
