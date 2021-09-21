"""empty message

Revision ID: a6d7de9f15fb
Revises: adef2cdc2bbe
Create Date: 2021-09-20 23:19:49.058486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6d7de9f15fb'
down_revision = 'adef2cdc2bbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('m_system_code_factory_cd_fkey', 'm_system_code', type_='foreignkey')
    op.create_foreign_key(None, 'm_system_code', 'm_factory', ['factory_cd'], ['factory_cd'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'm_system_code', type_='foreignkey')
    op.create_foreign_key('m_system_code_factory_cd_fkey', 'm_system_code', 'm_factory', ['factory_cd'], ['factory_cd'], ondelete='CASCADE')
    # ### end Alembic commands ###