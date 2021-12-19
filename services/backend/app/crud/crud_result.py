import io
from typing import Any, Dict, Optional, Union
from uuid import UUID

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.result import AnalysisResult
from app.schemas.analysis_result import (
    AnalysisResultCreate,
    AnalysisResultStatusUpdate,
    AnalysisResultUpdate,
)


class CRUDAnalysisResult(
    CRUDBase[AnalysisResult, AnalysisResultCreate, AnalysisResultUpdate]
):
    def get_by_patient_id(self, db: Session, patient_id: UUID):
        return (
            db.query(AnalysisResult)
            .filter(AnalysisResult.patient_id == patient_id)
            .all()
        )

    def create(self, db: Session, *, obj_in: AnalysisResultCreate) -> AnalysisResult:
        db_obj = AnalysisResult(
            status=obj_in.status,
            patient_id=obj_in.patient_id,
            recording_id=obj_in.recording_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_status(
        self, db: Session, *, db_obj: AnalysisResult, obj_in: AnalysisResultStatusUpdate
    ) -> AnalysisResult:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def update_data(
        self, db: Session, *, db_obj: AnalysisResult, obj_in: AnalysisResultUpdate
    ) -> AnalysisResult:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)


analysis_result = CRUDAnalysisResult(AnalysisResult)
