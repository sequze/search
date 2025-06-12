from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from models import db_helper
from core.search import search
from fastapi import Depends

router = APIRouter(tags=["Search"])

@router.get("/request")
async def index(request: str,
          postgres: AsyncSession = Depends(db_helper.postgres.session_getter),
          mysql: AsyncSession = Depends(db_helper.mysql.session_getter),
          ):
    return await search(
        request=request,
        limit=5,
        postgres_session=postgres,
        mysql_session=mysql,
    )
