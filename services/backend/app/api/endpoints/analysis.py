from typing import Any, List
from uuid import UUID
from app.schemas.analysis_result import AnalysisResultCreate

from fastapi import status


from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    File,
    UploadFile,
    BackgroundTasks,
)

from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.schemas.recording import RecordingCreate
from app.services.bowel_service import BowelAnalysisService
from app.worker import app as celery_ref

router = APIRouter()
from app.api import deps


@router.post("/recordings/upload")
async def upload_audio_file(
    *, db: Session = Depends(deps.get_db), file_in: UploadFile = File(...)
):
    data = await file_in.read()
    rec_create = RecordingCreate(blob=data, filename=file_in.filename)
    recording = crud.recording.create(db, obj_in=rec_create)
    return recording.id


@router.get("/recordings/{recording_id}")
def get_recording(
    *,
    db: Session = Depends(deps.get_db),
    recording_id: UUID,
):
    recording = crud.recording.get(db, recording_id)
    return recording.filename


@router.post("/recordings/{recording_id}/analyze", status_code=status.HTTP_202_ACCEPTED)
def perform_analysis(*, db: Session = Depends(deps.get_db), recording_id: UUID):
    db: Session
    for db in deps.get_db():
        analysis_create = AnalysisResultCreate(status="CREATED")
        result = crud.analysis_result.create(db, obj_in=analysis_create)
        celery_ref.send_file.delay(recording_id, result.id)
        return result.id


@router.get("/results/{analysis_id}")
def get_results(*, db: Session = Depends(deps.get_db), analysis_id: UUID):
    result = crud.analysis_result.get(db, analysis_id)
    return dict(id=result.id, status=result.status)


@router.get("/results/{analysis_id}/frames")
def get_results(*, db: Session = Depends(deps.get_db), analysis_id: UUID):
    result = crud.analysis_result.get(db, analysis_id)
    if result.status != "COMPLETED":
        raise HTTPException(
            status_code=404,
            detail="The analysis with given ID has not been finished yet",
        )
    return result.frames


@router.get("/results/{analysis_id}/statistics")
def get_results(*, db: Session = Depends(deps.get_db), analysis_id: UUID):
    result = crud.analysis_result.get(db, analysis_id)
    if result.status != "COMPLETED":
        raise HTTPException(
            status_code=404,
            detail="The analysis with given ID has not been finished yet",
        )
    return result.statistics


@router.get("/results/{analysis_id}/status")
def get_results(*, db: Session = Depends(deps.get_db), analysis_id: UUID):
    result = crud.analysis_result.get(db, analysis_id)
    return result.status
