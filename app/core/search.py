from models import db_helper, Request
from models.db_helpers import RequestMongoModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import re

# import asyncio

# async def search_postgres():
#     await db_helper.init()
#     async with db_helper.postgres.session_maker() as session:
#         async with db_helper.mysql.session_maker() as mysql_session:
#             await search("Как", limit=5, postgres_session=session, mysql_session=mysql_session)


async def search(
    page: int,
    size: int,
    request: str,
    limit: int,
    postgres_session: AsyncSession,
    mysql_session: AsyncSession,
):
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
    return result[offset_min:offset_max]


# def main():
#     asyncio.run(search_postgres())

# main()
