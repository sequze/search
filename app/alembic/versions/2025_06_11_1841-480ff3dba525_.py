"""empty message

Revision ID: 480ff3dba525
Revises: 4160fd479a25
Create Date: 2025-06-11 18:41:00.201098

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "480ff3dba525"
down_revision: Union[str, None] = "4160fd479a25"
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
    op.add_column("users", sa.Column("username", sa.String(), nullable=False))


def downgrade_postgres() -> None:
    """Downgrade postgres schema."""
    op.drop_column("users", "username")
