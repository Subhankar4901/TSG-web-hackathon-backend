"""empty message

Revision ID: 9140cc5c6bdf
Revises: fc1b32d61705
Create Date: 2021-12-14 19:15:39.041268

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9140cc5c6bdf'
down_revision = 'fc1b32d61705'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('type', sa.String(length=100), nullable=True))
    op.add_column('event', sa.Column('event_tags', sa.String(length=100), nullable=True))
    op.drop_column('event', 'event_type')
    op.drop_column('event', 'tags')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('tags', mysql.VARCHAR(length=20), nullable=True))
    op.add_column('event', sa.Column('event_type', mysql.VARCHAR(length=20), nullable=True))
    op.drop_column('event', 'event_tags')
    op.drop_column('event', 'type')
    # ### end Alembic commands ###
