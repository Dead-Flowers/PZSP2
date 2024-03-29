"""user sex and birth date

Revision ID: b976e217e3bb
Revises: cf583a64a768
Create Date: 2022-01-11 21:27:44.747194

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

from app.models.user import Sex


# revision identifiers, used by Alembic.
revision = "b976e217e3bb"
down_revision = "cf583a64a768"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    sex = ENUM(Sex, name="sex")
    sex.create(op.get_bind(), checkfirst=True)
    op.add_column("user", sa.Column("sex", sex))
    op.add_column("user", sa.Column("birth_date", sa.Date()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "birth_date")
    op.drop_column("user", "sex")
    sex = ENUM(Sex, name="sex")
    sex.drop(op.get_bind())
    # ### end Alembic commands ###
