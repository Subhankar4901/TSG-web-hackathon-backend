"""empty message

Revision ID: 2747065b4d34
Revises: 
Create Date: 2021-12-14 12:02:17.039439

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2747065b4d34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('introduction', sa.Text(), nullable=True))
    op.add_column('event', sa.Column('procedure', sa.Text(), nullable=True))
    op.add_column('event', sa.Column('jugde_criteria', sa.Text(), nullable=True))
    op.add_column('event', sa.Column('timeline', sa.Text(), nullable=True))
    op.add_column('event', sa.Column('venue', sa.String(length=200), nullable=True))
    op.drop_column('event', 'vaenue')
    op.drop_column('event', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('description', mysql.TEXT(), nullable=True))
    op.add_column('event', sa.Column('vaenue', mysql.VARCHAR(length=200), nullable=True))
    op.drop_column('event', 'venue')
    op.drop_column('event', 'timeline')
    op.drop_column('event', 'jugde_criteria')
    op.drop_column('event', 'procedure')
    op.drop_column('event', 'introduction')
    # ### end Alembic commands ###