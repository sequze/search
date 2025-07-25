from models import db_helper, Request
from models.db_helpers import RequestMongoModel
from .schemas import SearchRequest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import re


async def search(
    page: int,
    size: int,
    request: str,
    limit: int,
    postgres_session: AsyncSession,
    mysql_session: AsyncSession,
) -> SearchRequest:
    result = []
    regex = re.compile(f".*{re.escape(request)}.*", re.IGNORECASE)
    for i in (
        await postgres_session.scalars(
            select(Request).where(Request.name.like(f"%{request}%")).limit(limit)
        )
    ).all():
        result.append(i.name.strip())

    for i in (
        await mysql_session.scalars(
            select(Request).where(Request.name.like(f"%{request}%")).limit(limit)
        )
    ).all():
        result.append(i.name.strip())
    for i in (
        await RequestMongoModel.find({"name": {"$regex": regex}}).limit(limit).to_list()
    ):
        result.append(i.name.strip())
    offset_min = (page - 1) * size
    offset_max = page * size
    has_next = page * size < len(result)
    return SearchRequest(results=result[offset_min:offset_max], has_next=has_next)


# def main():
#     asyncio.run(search_postgres())

# main()
=======
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

