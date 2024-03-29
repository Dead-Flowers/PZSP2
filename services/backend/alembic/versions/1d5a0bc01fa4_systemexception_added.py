"""systemexception added

Revision ID: 1d5a0bc01fa4
Revises: c68880f126bc
Create Date: 2022-01-15 15:34:43.174120

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "1d5a0bc01fa4"
down_revision = "97b9e398ea57"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "systemexception",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("source", sa.String(), nullable=True),
        sa.Column("value", sa.String(), nullable=True),
        sa.Column("creation_date", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_systemexception_id"), "systemexception", ["id"], unique=False
    )
    op.create_index(
        op.f("ix_systemexception_source"), "systemexception", ["source"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_systemexception_source"), table_name="systemexception")
    op.drop_index(op.f("ix_systemexception_id"), table_name="systemexception")
    op.drop_table("systemexception")
    # ### end Alembic commands ###
