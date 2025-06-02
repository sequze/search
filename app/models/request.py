from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base


class Request(Base):
    name: Mapped[str] = mapped_column(String(255), nullable=False)
