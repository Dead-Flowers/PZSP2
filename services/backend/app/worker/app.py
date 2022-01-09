import io
import os
from app.api import deps
from app.schemas.analysis_result import (
    AnalysisResultStatusUpdate,
    AnalysisResultUpdate,
)
from app.services.bowel_service import BowelAnalysisService
from app import crud

from celery import Celery
from sqlalchemy.orm.session import Session

celery = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis;//localhost:6379"),
)


@celery.task(name="send_file")
def send_file(recording_id: str, analysis_id: str):
    db: Session
    for db in deps.get_db():
        analysis = crud.analysis_result.get(db, id=analysis_id)
        analysis_update_status = AnalysisResultStatusUpdate(status="PENDING")
        crud.analysis_result.update_status(
            db, db_obj=analysis, obj_in=analysis_update_status
        )

        recording = crud.recording.get(db, recording_id)
        service = BowelAnalysisService("http://bowelsound.ii.pw.edu.pl")
        image_bytes = io.BytesIO(recording.blob)
        try:
            service.upload_file(image_bytes.read())
        except Exception:
            pass

        bowel_ret_val = service.get_status()
        analysis_res_obj = AnalysisResultUpdate(
            status="COMPLETED", **bowel_ret_val.as_dict()
        )
        analysis = crud.analysis_result.get(db, id=analysis_id)
        result = crud.analysis_result.update(
            db, db_obj=analysis, obj_in=analysis_res_obj
        )
        return result.id


import app.worker.task_handers
