"""first revision

Revision ID: cf583a64a768
Revises: 
Create Date: 2022-01-09 16:19:07.231285

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "cf583a64a768"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column(
            "role",
            sa.Enum("Admin", "Doctor", "Patient", name="userrole"),
            nullable=False,
        ),
        sa.Column("pesel", sa.String(length=11), nullable=True),
        sa.Column("passport_num", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("second_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("doctor_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["doctor_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_first_name"), "user", ["first_name"], unique=False)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_index(op.f("ix_user_last_name"), "user", ["last_name"], unique=False)
    op.create_index(
        op.f("ix_user_passport_num"), "user", ["passport_num"], unique=False
    )
    op.create_index(op.f("ix_user_pesel"), "user", ["pesel"], unique=False)
    op.create_index(op.f("ix_user_second_name"), "user", ["second_name"], unique=False)
    op.create_table(
        "recording",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("filename", sa.String(), nullable=True),
        sa.Column("byte_length", sa.Integer(), nullable=False),
        sa.Column("blob", sa.LargeBinary(), nullable=False),
        sa.Column("creation_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column("patient_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["patient_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_recording_filename"), "recording", ["filename"], unique=False
    )
    op.create_index(op.f("ix_recording_id"), "recording", ["id"], unique=False)
    op.create_table(
        "analysisresult",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("created_date", sa.DateTime(), nullable=False),
        sa.Column("error", sa.String(), nullable=True),
        sa.Column("result", sa.Integer(), nullable=True),
        sa.Column("frames", sa.JSON(), nullable=True),
        sa.Column("statistics", sa.JSON(), nullable=True),
        sa.Column("patient_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("recording_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["patient_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["recording_id"],
            ["recording.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_analysisresult_id"), "analysisresult", ["id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_analysisresult_id"), table_name="analysisresult")
    op.drop_table("analysisresult")
    op.drop_index(op.f("ix_recording_id"), table_name="recording")
    op.drop_index(op.f("ix_recording_filename"), table_name="recording")
    op.drop_table("recording")
    op.drop_index(op.f("ix_user_second_name"), table_name="user")
    op.drop_index(op.f("ix_user_pesel"), table_name="user")
    op.drop_index(op.f("ix_user_passport_num"), table_name="user")
    op.drop_index(op.f("ix_user_last_name"), table_name="user")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_index(op.f("ix_user_first_name"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
