"""create image column in products

Revision ID: 5ddd680b0a65
Revises: 8e44a774443e
Create Date: 2026-03-27 18:12:37.218921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ddd680b0a65'
down_revision: Union[str, Sequence[str], None] = '8e44a774443e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.add_column("product_table",sa.column("img_url",sa.VARCHAR(50)))

