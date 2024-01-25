"""create students table

Revision ID: 5bb9eb5ff7df
Revises: bf6f6ceb948e
Create Date: 2024-01-23 18:08:15.534582

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bb9eb5ff7df'
down_revision: Union[str, None] = 'bf6f6ceb948e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("students",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement="auto"),
                    sa.Column("student_name", sa.String),
                    sa.Column("group_id", sa.String(4), sa.ForeignKey("groups.id"))
                    )


def downgrade() -> None:
    op.drop_table("students")
