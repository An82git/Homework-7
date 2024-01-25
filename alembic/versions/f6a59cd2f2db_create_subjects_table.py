"""create subjects table

Revision ID: f6a59cd2f2db
Revises: 9670a81a4b49
Create Date: 2024-01-23 18:08:46.653271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6a59cd2f2db'
down_revision: Union[str, None] = '9670a81a4b49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("subjects",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement="auto"),
                    sa.Column("subject_name", sa.String),
                    sa.Column("teacher_id", sa.Integer, sa.ForeignKey("teachers.id"))
                    )


def downgrade() -> None:
    op.drop_table("subjects")
