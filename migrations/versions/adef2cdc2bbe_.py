"""empty message

Revision ID: adef2cdc2bbe
Revises: 93bba9d1638a
Create Date: 2021-09-20 23:18:47.514153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adef2cdc2bbe'
down_revision = '93bba9d1638a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('m_system_code', sa.Column('factory_cd', sa.String(length=2), nullable=True))
    op.create_index(op.f('ix_m_system_code_factory_cd'), 'm_system_code', ['factory_cd'], unique=False)
    op.create_foreign_key(None, 'm_system_code', 'm_factory', ['factory_cd'], ['factory_cd'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'm_system_code', type_='foreignkey')
    op.drop_index(op.f('ix_m_system_code_factory_cd'), table_name='m_system_code')
    op.drop_column('m_system_code', 'factory_cd')
    # ### end Alembic commands ###
