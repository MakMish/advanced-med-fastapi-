"""create image column in products

Revision ID: 3b7f2744cb23
Revises: 5ddd680b0a65
Create Date: 2026-03-27 18:22:54.552212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b7f2744cb23'
down_revision: Union[str, Sequence[str], None] = '5ddd680b0a65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
