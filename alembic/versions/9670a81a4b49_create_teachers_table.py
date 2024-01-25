"""create teachers table

Revision ID: 9670a81a4b49
Revises: 5bb9eb5ff7df
Create Date: 2024-01-23 18:08:34.899445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9670a81a4b49'
down_revision: Union[str, None] = '5bb9eb5ff7df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("teachers",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement="auto"),
                    sa.Column("teacher_name", sa.String)
                    )


def downgrade() -> None:
    op.drop_table("teachers")
