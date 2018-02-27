"""empty message

Revision ID: 8955487b3bfb
Revises: 
Create Date: 2018-02-22 17:58:34.596886

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8955487b3bfb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('index', 'idd')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('index', sa.Column('idd', mysql.INTEGER(display_width=10), autoincrement=False, nullable=True))
    # ### end Alembic commands ###