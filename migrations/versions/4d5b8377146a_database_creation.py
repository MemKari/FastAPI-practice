"""database creation

Revision ID: 4d5b8377146a
Revises: 
Create Date: 2024-06-06 02:03:18.566434

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '4d5b8377146a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('Users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=30), nullable=False),
                    sa.Column('role', sa.String(length=30), nullable=False),
                    sa.Column('degree', sa.String(length=60), nullable=True),
                    sa.Column('email', sa.String(length=50), nullable=False),
                    sa.Column('registered_at', sa.DateTime(), nullable=False),
                    sa.Column('role_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['role_id'], ['Roles.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    op.create_table('Trades',
                    sa.Column('trade_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('currency', sa.String(length=15), nullable=False),
                    sa.Column('side', sa.String(length=15), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('amount', sa.Float(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
                    sa.PrimaryKeyConstraint('trade_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Trades')
    op.drop_table('Users')
    op.drop_table('Roles')
    # ### end Alembic commands ###
