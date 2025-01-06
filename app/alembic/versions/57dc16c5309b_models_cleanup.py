"""models-cleanup

Revision ID: 57dc16c5309b
Revises: f4191b392c44
Create Date: 2025-01-06 12:36:34.055780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '57dc16c5309b'
down_revision: Union[str, None] = 'f4191b392c44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('owner_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], name='item_owner_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='item_pkey')
    )
    # ### end Alembic commands ###
