from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base
from app.db.base import Base

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    if settings.DISABLE_MIGRATIONS:
        Base.metadata.create_all(bind=db.get_bind())

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            role=base.UserRole.Admin,
            pesel="12345678900",
        )
        user = crud.user.create(db, obj_in=user_in)
