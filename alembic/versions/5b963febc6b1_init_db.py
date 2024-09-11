"""init db

Revision ID: 5b963febc6b1
Revises: 
Create Date: 2024-06-17 13:38:31.299210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b963febc6b1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drop_managers',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('tg_id', sa.String(), nullable=True),
    sa.Column('referral', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_drop_managers_id'), 'drop_managers', ['id'], unique=False)
    op.create_table('forms_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_forms_statuses_id'), 'forms_statuses', ['id'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teams_id'), 'teams', ['id'], unique=False)
    op.create_table('to_do_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('login', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_to_do_category_id'), 'to_do_category', ['id'], unique=False)
    op.create_table('training_folder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('folder_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_training_folder_id'), 'training_folder', ['id'], unique=False)
    op.create_table('forms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('dateBirth', sa.String(), nullable=True),
    sa.Column('year', sa.String(), nullable=True),
    sa.Column('passportWho', sa.String(), nullable=True),
    sa.Column('passportDetail', sa.String(), nullable=True),
    sa.Column('passportAddress', sa.String(), nullable=True),
    sa.Column('passportAddressOld', sa.String(), nullable=True),
    sa.Column('addressIndex', sa.String(), nullable=True),
    sa.Column('placeBirth', sa.String(), nullable=True),
    sa.Column('busPrice', sa.String(), nullable=True),
    sa.Column('metroPrice', sa.String(), nullable=True),
    sa.Column('job', sa.String(), nullable=True),
    sa.Column('transferWho', sa.String(), nullable=True),
    sa.Column('tenPayments', sa.String(), nullable=True),
    sa.Column('salary', sa.String(), nullable=True),
    sa.Column('ATMaddress', sa.String(), nullable=True),
    sa.Column('bankGadgetPast', sa.String(), nullable=True),
    sa.Column('bankDeposit', sa.String(), nullable=True),
    sa.Column('education', sa.String(), nullable=True),
    sa.Column('BankCardCity', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('addressPeople', sa.String(), nullable=True),
    sa.Column('bankClientAt', sa.String(), nullable=True),
    sa.Column('bankCredit', sa.String(), nullable=True),
    sa.Column('bankPersonVisit', sa.String(), nullable=True),
    sa.Column('bankGadget', sa.String(), nullable=True),
    sa.Column('bankEmail', sa.String(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('floorCount', sa.String(), nullable=True),
    sa.Column('bankNumberNow', sa.String(), nullable=True),
    sa.Column('bankNumberPast', sa.String(), nullable=True),
    sa.Column('cardDetail', sa.String(), nullable=True),
    sa.Column('additional', sa.String(), nullable=True),
    sa.Column('images', sa.String(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('drop_manager_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['drop_manager_id'], ['drop_managers.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['forms_statuses.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_forms_id'), 'forms', ['id'], unique=False)
    op.create_table('training_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('folder_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('route', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['folder_id'], ['training_folder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_training_file_id'), 'training_file', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('activeTeam', sa.String(), nullable=True),
    sa.Column('online', sa.Boolean(), nullable=True),
    sa.Column('active_team_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['active_team_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('forms_history',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('form_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['form_id'], ['forms.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_forms_history_id'), 'forms_history', ['id'], unique=False)
    op.create_table('to_do_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['to_do_category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_to_do_list_id'), 'to_do_list', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_to_do_list_id'), table_name='to_do_list')
    op.drop_table('to_do_list')
    op.drop_index(op.f('ix_forms_history_id'), table_name='forms_history')
    op.drop_table('forms_history')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_training_file_id'), table_name='training_file')
    op.drop_table('training_file')
    op.drop_index(op.f('ix_forms_id'), table_name='forms')
    op.drop_table('forms')
    op.drop_index(op.f('ix_training_folder_id'), table_name='training_folder')
    op.drop_table('training_folder')
    op.drop_index(op.f('ix_to_do_category_id'), table_name='to_do_category')
    op.drop_table('to_do_category')
    op.drop_index(op.f('ix_teams_id'), table_name='teams')
    op.drop_table('teams')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_forms_statuses_id'), table_name='forms_statuses')
    op.drop_table('forms_statuses')
    op.drop_index(op.f('ix_drop_managers_id'), table_name='drop_managers')
    op.drop_table('drop_managers')
    # ### end Alembic commands ###