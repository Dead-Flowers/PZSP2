import io
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.result import AnalysisResult
from app.schemas.analysis_result import AnalysisResultCreate


class CRUDAnalysisResult(CRUDBase[AnalysisResult, AnalysisResultCreate, None]):
    def create(self, db: Session, *, obj_in: AnalysisResultCreate) -> AnalysisResult:
        db_obj = AnalysisResult(**obj_in.get_status_return_value.as_dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


analysis_result = CRUDAnalysisResult(AnalysisResult)
