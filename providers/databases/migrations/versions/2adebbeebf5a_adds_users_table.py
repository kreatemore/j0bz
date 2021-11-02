"""Adds users table

Revision ID: 2adebbeebf5a
Revises: 
Create Date: 2021-11-02 08:47:08.890647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2adebbeebf5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=256), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email_address', sa.Unicode(length=256), nullable=False),
    sa.Column('type', sa.Enum('employer', 'candidate', name='usertype'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stripe_users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stripe_users')
    op.drop_table('users')
    # ### end Alembic commands ###
