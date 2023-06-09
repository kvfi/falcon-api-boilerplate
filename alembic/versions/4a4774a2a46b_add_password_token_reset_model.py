"""add password token reset model

Revision ID: 4a4774a2a46b
Revises: 7ddaf5286202
Create Date: 2023-04-09 18:06:57.573161

"""
from alembic import op
import sqlalchemy as sa
from pathlib import Path

# revision identifiers, used by Alembic.
revision = '4a4774a2a46b'
down_revision = '7ddaf5286202'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('password_reset_token',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('token', sa.String(), nullable=False),
                    sa.Column('created_on', sa.DateTime(), nullable=False),
                    sa.Column('expires_on', sa.DateTime(), nullable=False),
                    sa.Column('used_on', sa.DateTime(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('password_reset_token')
    # ### end Alembic commands ###
