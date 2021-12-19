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

def check_doctor(db: Session=Depends(deps.get_db), doctor_id: UUID=None, patient_id: UUID=None) -> bool:
    patients = crud.user.get_by_doctor_id(db, doctor_id)
    ids = [patient.id for patient in patients]
    if(patient_id not in ids):
        return False
    return True

@router.post("/recordings/upload")
async def upload_audio_file(
    *, db: Session = Depends(deps.get_db), 
    current_user: models.User = Depends(deps.get_current_user),
    patient_id: UUID, 
    file_in: UploadFile = File(...)
):
    print(current_user.id)
    print(patient_id)
    if not crud.user.has_roles(current_user, models.UserRole.Admin) and not check_doctor(db, current_user.id, patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access this patient"
        )
    data = await file_in.read()
    rec_create = RecordingCreate(blob=data, patient_id=patient_id, filename=file_in.filename)
    recording = crud.recording.create(db, obj_in=rec_create)
    return recording.id


@router.get("/recordings/{recording_id}")
def get_recording(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    recording_id: UUID,
):
    recording = crud.recording.get(db, recording_id)
    patient_id = recording.patient_id
    if not crud.user.has_roles(current_user, models.UserRole.Admin) and not check_doctor(db, current_user.id, patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access this patient"
        )
    return dict(id=recording.id, filename=recording.filename, patient_id=recording.patient_id, byte_length=recording.byte_length)


@router.get("/recordings")
def get_recordings(
    *, 
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    patient_id: UUID=None, 
    skip: int = 0,
    limit: int = 100
):
    if not crud.user.has_roles(current_user, models.UserRole.Admin) and patient_id is None:
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access all recordings"
        )
    elif crud.user.has_roles(current_user, models.UserRole.Doctor) and not check_doctor(db, current_user.id, patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access this recording"
        )
    if patient_id is None:
        recordings = crud.recording.get_multi(db, skip, limit)
    else:
        recordings = crud.recording.get_by_patient_id(db, patient_id)
    recs = []
    for rec in recordings:
        recs.append(dict(id=rec.id, filename=rec.filename, creation_date=rec.creation_date, patient_id=rec.patient_id))
    return recs


@router.post("/recordings/{recording_id}/analyze", status_code=status.HTTP_202_ACCEPTED)
def perform_analysis(
    *, 
    db: Session = Depends(deps.get_db), 
    current_user: models.User = Depends(deps.get_current_user),
    recording_id: UUID
):    
    db: Session
    for db in deps.get_db():
        recording = crud.recording.get(db, recording_id)
        if not crud.user.has_roles(current_user, models.UserRole.Admin) and not check_doctor(db, current_user.id, recording.patient_id):
            raise HTTPException(
                status_code=403,
                detail="Insufficient privilages to access this recording"
            )
        analysis_create = AnalysisResultCreate(status="CREATED", patient_id=recording.patient_id, recording_id=recording_id)
        result = crud.analysis_result.create(db, obj_in=analysis_create)
        celery_ref.send_file.delay(recording_id, result.id)
        return result.id


@router.get("/results/{analysis_id}")
def get_results(
    *, 
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user), 
    analysis_id: UUID
):
    result = crud.analysis_result.get(db, analysis_id)
    if not crud.user.has_roles(current_user, models.UserRole.Admin) and not check_doctor(db, current_user.id, result.patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access this analysis result"
        )
    return dict(id=result.id, status=result.status)


@router.get("/results/{analysis_id}/frames")
def get_results(
    *, 
    db: Session = Depends(deps.get_db), 
    current_user: models.User = Depends(deps.get_current_user),
    analysis_id: UUID
):
    result = crud.analysis_result.get(db, analysis_id)
    if not crud.user.has_roles(current_user, models.UserRole.Admin) and not check_doctor(db, current_user.id, result.patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access this analysis result"
        )
    if result.status != "COMPLETED":
        raise HTTPException(
            status_code=404,
            detail="The analysis with given ID has not been finished yet",
        )
    return result.frames


@router.get("/results/{analysis_id}/statistics")
def get_results(
    *, 
    db: Session = Depends(deps.get_db), 
    current_user: models.User = Depends(deps.get_current_user),
    analysis_id: UUID
):
    result = crud.analysis_result.get(db, analysis_id)
    if not crud.user.has_roles(current_user, models.UserRole.Admin) and not check_doctor(db, current_user.id, result.patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access this analysis result"
        )
    if result.status != "COMPLETED":
        raise HTTPException(
            status_code=404,
            detail="The analysis with given ID has not been finished yet",
        )
    return result.statistics


@router.get("/results/{analysis_id}/status")
def get_results(
    *, 
    db: Session = Depends(deps.get_db), 
    current_user: models.User = Depends(deps.get_current_user),
    analysis_id: UUID
):
    result = crud.analysis_result.get(db, analysis_id)
    if not crud.user.has_roles(current_user, models.UserRole.Admin) and not check_doctor(db, current_user.id, result.patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access this analysis result"
        )
    return result.status


@router.get("/results")
def get_results(
    *, 
    db: Session = Depends(deps.get_db), 
    current_user: models.User = Depends(deps.get_current_user),
    patient_id: UUID = None, 
    skip: int = 0, 
    limit: int = 100
):
    if not crud.user.has_roles(current_user, models.UserRole.Admin) and patient_id is None:
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access all results"
        )
    elif crud.user.has_roles(current_user, models.UserRole.Doctor) and not check_doctor(db, current_user.id, patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privilages to access this patient's results"
        )
    if patient_id is None:
        results = crud.analysis_result.get_multi(db, skip, limit)
    else:
        results = crud.analysis_result.get_by_patient_id(db, patient_id)
    filtered_results = []
    for result in results:
        filtered_results.append(dict(id=result.id, status=result.status, patient_id=result.patient_id, created_date=result.created_date, recording_id=result.recording_id))
    return filtered_results