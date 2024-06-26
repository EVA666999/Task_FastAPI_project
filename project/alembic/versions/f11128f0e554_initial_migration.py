"""initial migration

Revision ID: f11128f0e554
Revises: 034612cf879c
Create Date: 2024-05-08 03:27:38.715913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f11128f0e554'
down_revision: Union[str, None] = '034612cf879c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_task_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'task_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('task_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_task_id_fkey', 'users', 'task', ['task_id'], ['id'])
    # ### end Alembic commands ###
