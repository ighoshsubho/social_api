"""Add content column to post table

Revision ID: 4825595afc24
Revises: 8aa3bab05184
Create Date: 2022-11-03 20:17:13.934546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4825595afc24'
down_revision = '8aa3bab05184'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass