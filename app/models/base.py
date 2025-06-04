from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column
)
from sqlalchemy import MetaData
from config import settings


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    __abstract__ = True
    metadata = MetaData(
        naming_convention=settings.naming_convention,
    )

    id: Mapped[int] = mapped_column(primary_key=True)
