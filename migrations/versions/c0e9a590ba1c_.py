"""empty message

Revision ID: c0e9a590ba1c
Revises: 5c44727f799d
Create Date: 2023-08-30 00:35:20.270932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0e9a590ba1c'
down_revision = '5c44727f799d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('character_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('vehicle_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('film_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'characters', ['character_id'], ['id'])
        batch_op.create_foreign_key(None, 'vehicle', ['vehicle_id'], ['id'])
        batch_op.create_foreign_key(None, 'films', ['film_id'], ['id'])
        batch_op.create_foreign_key(None, 'planets', ['planet_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('film_id')
        batch_op.drop_column('vehicle_id')
        batch_op.drop_column('planet_id')
        batch_op.drop_column('character_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
