"""empty message

Revision ID: 80cc56b30e10
Revises: 8955487b3bfb
Create Date: 2018-02-22 18:22:39.977945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80cc56b30e10'
down_revision = '8955487b3bfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('index', sa.Column('idd', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('index', 'idd')
    # ### end Alembic commands ###
