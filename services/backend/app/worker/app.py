import io
import os
from app.api import deps
from app.schemas.analysis_result import (
    AnalysisResultStatusUpdate,
    AnalysisResultUpdate,
)
from app.services.bowel_service import BowelAnalysisService
from app import crud

from celery import Celery, Task
from sqlalchemy.orm.session import Session

celery = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
)


@celery.task(
    bind=True,
    name="send_file",
    max_retries=5,
    retry_backoff=True,
    default_retry_delay=10,
    acks_late=True,
)
def send_file(self: Task, recording_id: str, analysis_id: str):
    db: Session

    def update_state(new_state, **kwargs):
        analysis_update_status = AnalysisResultUpdate(status=new_state, **kwargs)
        analysis = crud.analysis_result.get(db, id=analysis_id)
        result = crud.analysis_result.update(
            db, db_obj=analysis, obj_in=analysis_update_status
        )
        self.send_event('task-analysis-status', analysis_id=analysis_id, state=new_state)
        return result
        

    for db in  deps.get_db():
        update_state('PENDING')

        recording = crud.recording.get(db, recording_id)
        service = BowelAnalysisService("http://bowelsound.ii.pw.edu.pl")
        image_bytes = io.BytesIO(recording.blob)
        try:
            service.upload_file(image_bytes.read())
        except Exception as e:
            if self.max_retries == self.request.retries:
                update_state('FAILED')

            self.retry(exc=e)

        bowel_ret_val = service.get_status()
        result = update_state('COMPLETED', **bowel_ret_val.as_dict())
        return result.id


import app.worker.task_handers
