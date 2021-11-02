"""empty message

Revision ID: aa7995b45696
Revises: 2adebbeebf5a
Create Date: 2021-11-02 09:10:49.136984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa7995b45696'
down_revision = '2adebbeebf5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stripe_users', sa.Column('stripe_customer_id', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stripe_users', 'stripe_customer_id')
    # ### end Alembic commands ###