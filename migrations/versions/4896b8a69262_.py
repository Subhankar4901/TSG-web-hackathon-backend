"""empty message

Revision ID: 4896b8a69262
Revises: 9140cc5c6bdf
Create Date: 2021-12-14 19:50:02.671374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4896b8a69262'
down_revision = '9140cc5c6bdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('participation_certificate', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'participation_certificate')
    # ### end Alembic commands ###
