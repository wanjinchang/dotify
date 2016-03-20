"""empty message

Revision ID: 1e3e5c3ccab
Revises: None
Create Date: 2016-03-21 22:10:44.539638

"""

# revision identifiers, used by Alembic.
revision = '1e3e5c3ccab'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('countries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('value', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operators',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('value', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('artist', sa.String(length=255), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('country_vectors',
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('dim_0', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_1', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_2', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_3', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_4', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_5', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_6', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_7', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_8', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_9', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_10', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_11', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_12', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_13', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_14', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_15', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_16', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_17', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_18', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_19', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_20', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_21', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_22', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_23', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_24', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_25', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_26', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_27', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_28', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_29', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['countries.id'], ),
    sa.PrimaryKeyConstraint('country_id')
    )
    op.create_table('song_vectors',
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('dim_0', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_1', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_2', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_3', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_4', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_5', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_6', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_7', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_8', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_9', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_10', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_11', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_12', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_13', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_14', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_15', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_16', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_17', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_18', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_19', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_20', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_21', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_22', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_23', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_24', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_25', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_26', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_27', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_28', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.Column('dim_29', sa.Float(precision=11, decimal_return_scale=10), nullable=True),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('song_id')
    )
    op.create_table('top_songs',
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('streams', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['countries.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('song_id', 'country_id', 'rank', 'date')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('top_songs')
    op.drop_table('song_vectors')
    op.drop_table('country_vectors')
    op.drop_table('songs')
    op.drop_table('operators')
    op.drop_table('countries')
    ### end Alembic commands ###
