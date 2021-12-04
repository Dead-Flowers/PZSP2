import io
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.result import AnalysisResult
from app.schemas.analysis_result import AnalysisResultCreate, AnalysisResultStatusUpdate, AnalysisResultUpdate


class CRUDAnalysisResult(CRUDBase[AnalysisResult, AnalysisResultCreate, AnalysisResultUpdate]):
    def create(self, db: Session, *, obj_in: AnalysisResultCreate) -> AnalysisResult:
        db_obj = AnalysisResult(status=obj_in.status)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_status(self, db: Session, *, db_obj: AnalysisResult, obj_in: AnalysisResultStatusUpdate) -> AnalysisResult:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def update_data(self, db: Session, *, db_obj: AnalysisResult, obj_in: AnalysisResultUpdate) -> AnalysisResult:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

analysis_result = CRUDAnalysisResult(AnalysisResult)
