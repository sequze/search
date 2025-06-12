"""user table

Revision ID: 4160fd479a25
Revises: 453289b9d1aa
Create Date: 2025-06-11 17:59:01.955425

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4160fd479a25"
down_revision: Union[str, None] = "453289b9d1aa"
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
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)


def downgrade_postgres() -> None:
    """Downgrade postgres schema."""
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
