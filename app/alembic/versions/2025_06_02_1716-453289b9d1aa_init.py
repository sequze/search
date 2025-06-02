"""init

Revision ID: 453289b9d1aa
Revises:
Create Date: 2025-06-02 17:16:19.488336

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "453289b9d1aa"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    """Upgrade schema."""
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    """Downgrade schema."""
    globals()["downgrade_%s" % engine_name]()


def upgrade_postgres() -> None:
    """Upgrade postgres schema."""
    op.create_table(
        "requests",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_requests")),
    )


def downgrade_postgres() -> None:
    """Downgrade postgres schema."""
    op.drop_table("requests")


def upgrade_mysql() -> None:
    """Upgrade mysql schema."""
    op.create_table(
        "requests",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_requests")),
    )


def downgrade_mysql() -> None:
    """Downgrade mysql schema."""
    op.drop_table("requests")
