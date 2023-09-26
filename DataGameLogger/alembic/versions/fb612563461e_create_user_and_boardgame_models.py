"""Create user and boardgame models

Revision ID: fb612563461e
Revises: 
Create Date: 2023-09-26 19:19:46.944157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb612563461e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('user_boardgame_collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_bgg', sa.Integer(), nullable=True),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'id_user')
    )
    op.create_index(op.f('ix_user_boardgame_collection_id'), 'user_boardgame_collection', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_boardgame_collection_id'), table_name='user_boardgame_collection')
    op.drop_table('user_boardgame_collection')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
