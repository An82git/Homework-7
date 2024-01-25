"""create assessments table

Revision ID: f6b128d4ebff
Revises: f6a59cd2f2db
Create Date: 2024-01-23 18:08:57.899958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6b128d4ebff'
down_revision: Union[str, None] = 'f6a59cd2f2db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("assessments",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement="auto"),
                    sa.Column("student_id", sa.Integer, sa.ForeignKey("students.id")),
                    sa.Column("subject_id", sa.Integer, sa.ForeignKey("subjects.id")),
                    sa.Column("assessment", sa.Integer),
                    sa.Column("date_of_receipt", sa.DATE)
                    )


def downgrade() -> None:
    op.drop_table("assessments")
