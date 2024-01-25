"""create groups table

Revision ID: bf6f6ceb948e
Revises: 
Create Date: 2024-01-22 18:20:29.373638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf6f6ceb948e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("groups", 
                    sa.Column("id", sa.String(4), primary_key=True),
                    sa.Column("group_name", sa.String)
                    )


def downgrade() -> None:
    op.drop_table("groups")
