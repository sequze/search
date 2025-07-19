from models import db_helper, Request
from models.db_helpers import RequestMongoModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import re


async def search(
    request: str,
    limit: int,
    postgres_session: AsyncSession,
    mysql_session: AsyncSession,
):
    result = []
    regex = re.compile(f".*{re.escape(request)}.*", re.IGNORECASE)
    result.append(
        [i.name.strip() for i in (
                await postgres_session.scalars(
                    select(Request)
                    .where(Request.name.like(f"%{request}%"))
                    .limit(limit)
                )).all()
        ]
    )
    result.append(
        [i.name.strip() for i in (
                await mysql_session.scalars(
                    select(Request)
                    .where(Request.name.like(f"%{request}%"))
                    .limit(limit)
                )).all()
        ]
    )
    result.append(
        [
            i.name.strip()
            for i in await RequestMongoModel.find({"name": {"$regex": regex}})
            .limit(limit)
            .to_list()
        ]
    )
    return result
