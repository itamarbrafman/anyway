"""type to resolution column name

Revision ID: 5fd0841324e2
Revises: 4351468c3446
Create Date: 2023-08-17 11:15:35.015587

"""

# revision identifiers, used by Alembic.
revision = '5fd0841324e2'
down_revision = '4351468c3446'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('resolution', sa.Enum('REGION', 'DISTRICT', 'CITY', 'STREET', 'URBAN_JUNCTION', 'SUBURBAN_ROAD', 'SUBURBAN_JUNCTION', 'OTHER', name='resolutioncategories'), nullable=False))
    op.create_index(op.f('ix_comments_resolution'), 'comments', ['resolution'], unique=False)
    op.drop_index('ix_comments_type', table_name='comments')
    op.drop_column('comments', 'type')

    # ### end Alembic commands ###