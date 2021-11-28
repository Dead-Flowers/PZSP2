import io
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.recording import Recording
from app.schemas.recording import RecordingCreate


class CRUDRecording(CRUDBase[Recording, RecordingCreate, None]):
    def create(self, db: Session, *, obj_in: RecordingCreate) -> Recording:
        db_obj = Recording(
            filename=obj_in.filename,
            byte_length=len(obj_in.blob),
            blob=obj_in.blob,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


recording = CRUDRecording(Recording)
