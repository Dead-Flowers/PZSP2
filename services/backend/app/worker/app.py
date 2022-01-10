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

    def update_state_obj(update_obj):
        analysis = crud.analysis_result.get(db, id=analysis_id)
        result = crud.analysis_result.update(
            db, db_obj=analysis, obj_in=update_obj
        )
        self.send_event('task-analysis-status', analysis_id=analysis_id, state=update_obj.status)
        return result

    def update_state(new_state):
        analysis_update = AnalysisResultStatusUpdate(status=new_state)
        return update_state_obj(analysis_update)
    
    def handle():
        update_state('PENDING')

        service = BowelAnalysisService("http://bowelsound.ii.pw.edu.pl")
        recording = crud.recording.get(db, recording_id)
        image_bytes = io.BytesIO(recording.blob)

        service.upload_file(image_bytes.read())

        bowel_ret_val = service.get_status()
        result = update_state_obj(AnalysisResultUpdate(status='COMPLETED', **bowel_ret_val.as_dict()))

        return result.id

    for db in deps.get_db():
        try:
            return handle()
        except Exception as e:
            try:
                if self.max_retries == self.request.retries:
                    update_state('FAILED')
                else:
                    update_state('RETRYING')
            except: # updating state can go wrong
                pass
            self.retry(exc=e)
    return None


import app.worker.task_handers
