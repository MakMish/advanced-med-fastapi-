"""upgrade to indexing

Revision ID: 75a6b586fc80
Revises: 3b7f2744cb23
Create Date: 2026-04-09 15:02:38.227104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75a6b586fc80'
down_revision: Union[str, Sequence[str], None] = '3b7f2744cb23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index("idx_2","user_table",["uemail"],unique=True)
    print("successfully executed")
def downgrade() -> None:
    """Downgrade schema."""
   