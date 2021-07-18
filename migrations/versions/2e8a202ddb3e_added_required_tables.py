"""Added required tables

Revision ID: 2e8a202ddb3e
Revises: 
Create Date: 2021-07-18 23:10:07.817028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e8a202ddb3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('town',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('current_weather', sa.String(), nullable=True),
    sa.Column('forecast_weather', sa.String(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_town_id'), 'town', ['id'], unique=False)
    op.create_index(op.f('ix_town_name'), 'town', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_town_name'), table_name='town')
    op.drop_index(op.f('ix_town_id'), table_name='town')
    op.drop_table('town')
    # ### end Alembic commands ###