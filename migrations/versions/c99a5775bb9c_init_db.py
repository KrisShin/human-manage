"""init db

Revision ID: c99a5775bb9c
Revises: 
Create Date: 2021-09-18 23:02:01.876950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c99a5775bb9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('m_factory',
    sa.Column('abort_div', sa.Integer(), nullable=True),
    sa.Column('update_user_id', sa.String(length=32), nullable=True),
    sa.Column('update_count', sa.Integer(), nullable=True),
    sa.Column('update_pgid', sa.String(length=512), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('factory_cd', sa.String(length=2), nullable=False),
    sa.Column('factory_nm', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('factory_cd')
    )
    op.create_index(op.f('ix_m_factory_abort_div'), 'm_factory', ['abort_div'], unique=False)
    op.create_table('m_calendar',
    sa.Column('abort_div', sa.Integer(), nullable=True),
    sa.Column('update_user_id', sa.String(length=32), nullable=True),
    sa.Column('update_count', sa.Integer(), nullable=True),
    sa.Column('update_pgid', sa.String(length=512), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('calendar_date', sa.String(length=8), nullable=False),
    sa.Column('Seq_No', sa.Integer(), nullable=False),
    sa.Column('holiday_flg', sa.Integer(), nullable=True),
    sa.Column('holiday_nm', sa.String(length=10), nullable=True),
    sa.Column('event_cd', sa.Integer(), nullable=True),
    sa.Column('event_nm', sa.String(length=20), nullable=True),
    sa.Column('event_time1', sa.String(length=4), nullable=False),
    sa.Column('event_time2', sa.String(length=4), nullable=False),
    sa.Column('month_end_flg', sa.String(length=1), nullable=True),
    sa.Column('sche_flg', sa.String(length=1), nullable=True),
    sa.Column('factory_cd', sa.String(length=2), nullable=True),
    sa.ForeignKeyConstraint(['factory_cd'], ['m_factory.factory_cd'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('calendar_date', 'Seq_No')
    )
    op.create_index(op.f('ix_m_calendar_abort_div'), 'm_calendar', ['abort_div'], unique=False)
    op.create_index(op.f('ix_m_calendar_event_cd'), 'm_calendar', ['event_cd'], unique=False)
    op.create_index(op.f('ix_m_calendar_factory_cd'), 'm_calendar', ['factory_cd'], unique=False)
    op.create_index(op.f('ix_m_calendar_holiday_flg'), 'm_calendar', ['holiday_flg'], unique=False)
    op.create_table('m_department',
    sa.Column('dep_cd', sa.String(length=10), nullable=False),
    sa.Column('dep_name', sa.String(length=64), nullable=True),
    sa.Column('factory_cd', sa.String(length=2), nullable=True),
    sa.ForeignKeyConstraint(['factory_cd'], ['m_factory.factory_cd'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('dep_cd')
    )
    op.create_index(op.f('ix_m_department_factory_cd'), 'm_department', ['factory_cd'], unique=False)
    op.create_table('m_system_code',
    sa.Column('abort_div', sa.Integer(), nullable=True),
    sa.Column('update_user_id', sa.String(length=32), nullable=True),
    sa.Column('update_count', sa.Integer(), nullable=True),
    sa.Column('update_pgid', sa.String(length=512), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('code_kbn', sa.String(length=3), nullable=False),
    sa.Column('code_kbn_nm', sa.String(length=10), nullable=True),
    sa.Column('code_no', sa.String(length=3), nullable=False),
    sa.Column('code_nm', sa.String(length=10), nullable=True),
    sa.Column('flug1', sa.String(length=1), nullable=True),
    sa.Column('flug1_nm', sa.String(length=10), nullable=True),
    sa.Column('flug2', sa.String(length=1), nullable=True),
    sa.Column('flug2_nm', sa.String(length=10), nullable=True),
    sa.Column('flug3', sa.String(length=1), nullable=True),
    sa.Column('flug3_nm', sa.String(length=100), nullable=True),
    sa.Column('factory_cd', sa.String(length=2), nullable=True),
    sa.ForeignKeyConstraint(['factory_cd'], ['m_factory.factory_cd'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('code_kbn', 'code_no')
    )
    op.create_index(op.f('ix_m_system_code_abort_div'), 'm_system_code', ['abort_div'], unique=False)
    op.create_index(op.f('ix_m_system_code_factory_cd'), 'm_system_code', ['factory_cd'], unique=False)
    op.create_table('m_user',
    sa.Column('user_cd', sa.String(length=6), nullable=False),
    sa.Column('user_nm', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=512), nullable=True),
    sa.Column('role_cd', sa.Integer(), nullable=False),
    sa.Column('duty_cd', sa.String(length=2), nullable=True),
    sa.Column('create_user_id', sa.String(length=6), nullable=True),
    sa.Column('dep_cd', sa.String(length=10), nullable=True),
    sa.Column('factory_cd', sa.String(length=2), nullable=True),
    sa.ForeignKeyConstraint(['dep_cd'], ['m_department.dep_cd'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['factory_cd'], ['m_factory.factory_cd'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_cd')
    )
    op.create_index(op.f('ix_m_user_dep_cd'), 'm_user', ['dep_cd'], unique=False)
    op.create_index(op.f('ix_m_user_factory_cd'), 'm_user', ['factory_cd'], unique=False)
    op.create_index(op.f('ix_m_user_role_cd'), 'm_user', ['role_cd'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_m_user_role_cd'), table_name='m_user')
    op.drop_index(op.f('ix_m_user_factory_cd'), table_name='m_user')
    op.drop_index(op.f('ix_m_user_dep_cd'), table_name='m_user')
    op.drop_table('m_user')
    op.drop_index(op.f('ix_m_system_code_factory_cd'), table_name='m_system_code')
    op.drop_index(op.f('ix_m_system_code_abort_div'), table_name='m_system_code')
    op.drop_table('m_system_code')
    op.drop_index(op.f('ix_m_department_factory_cd'), table_name='m_department')
    op.drop_table('m_department')
    op.drop_index(op.f('ix_m_calendar_holiday_flg'), table_name='m_calendar')
    op.drop_index(op.f('ix_m_calendar_factory_cd'), table_name='m_calendar')
    op.drop_index(op.f('ix_m_calendar_event_cd'), table_name='m_calendar')
    op.drop_index(op.f('ix_m_calendar_abort_div'), table_name='m_calendar')
    op.drop_table('m_calendar')
    op.drop_index(op.f('ix_m_factory_abort_div'), table_name='m_factory')
    op.drop_table('m_factory')
    # ### end Alembic commands ###
