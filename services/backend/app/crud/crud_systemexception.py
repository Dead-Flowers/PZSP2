from app.crud.base import CRUDBase, ModelType
from app.models.systemexception import SystemException
from app.schemas.systemexception import SystemExceptionCreate
from typing import List
from sqlalchemy.orm import Session


class CRUDSystemException(CRUDBase[SystemException, SystemExceptionCreate, None]):
    def create(self, db: Session, obj_in: SystemExceptionCreate) -> SystemException:
        db_obj = SystemException(source=obj_in.source, value=obj_in.value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, skip: int = 0, limit: int = 25
    ) -> List[SystemException]:
        return (
            db.query(SystemException)
            .order_by(SystemException.creation_date.desc())
            .limit(limit)
            .all()
        )


system_exception = CRUDSystemException(SystemException)
