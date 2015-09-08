"""add ip address to database

Revision ID: 2afbc7d30a21
Revises: 41c29db70997
Create Date: 2015-09-08 21:19:59.721831

"""

# revision identifiers, used by Alembic.
revision = '2afbc7d30a21'
down_revision = '41c29db70997'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('PiUrl', sa.Column('ip', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('PiUrl', 'ip')
    ### end Alembic commands ###
