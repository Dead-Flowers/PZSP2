import io
import time
import os
from app.api import deps
from app.schemas.analysis_result import AnalysisResultCreate
from app.services.bowel_service import BowelAnalysisService
from app import crud

from celery import Celery
from sqlalchemy.orm.session import Session

celery = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis;//localhost:6379"),
)


@celery.task(name="analyze")
def perform_analysis(task_type):
    time.sleep(5)
    return True


@celery.task(name="add")
def add(a, b):
    time.sleep(3)
    return a + b


@celery.task(name="send_file")
def send_file(recording_id):
    db: Session
    for db in deps.get_db():
        recording = crud.recording.get(db, recording_id)
        service = BowelAnalysisService("http://bowelsound.ii.pw.edu.pl")
        imageBytes = io.BytesIO(recording.blob)
        service.upload_file(imageBytes.read())
        ret_val = service.get_status()
        db: Session
        for db in deps.get_db():
            ret_value = AnalysisResultCreate(get_status_return_value=ret_val)
            result = crud.analysis_result.create(db, obj_in=ret_value)
            return result.id


import app.worker.task_handers
