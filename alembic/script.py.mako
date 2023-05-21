"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
from pathlib import Path
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    ${upgrades if upgrades else "pass"}

    with open(str(Path(__file__).with_suffix('')) + '_up.sql', 'r') as f:
        op.execute(f.read())


def downgrade():
    ${downgrades if downgrades else "pass"}

    with open(str(Path(__file__).with_suffix('')) + '_down.sql', 'r') as f:
        op.execute(f.read())
