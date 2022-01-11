from typing import Optional
from uuid import UUID
from app.schemas.analysis_result import AnalysisResultCreate

from fastapi import status, WebSocket


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
from app.services.ws_manager import manager as ws_manager

from app.api import deps

router = APIRouter()


def can_access_results(db: Session, user: models.User, patient_id: Optional[UUID]):
    if patient_id is None:
        return crud.user.has_roles(user, models.UserRole.Admin)

    return (
        crud.user.has_roles(user, models.UserRole.Admin)
        or (
            crud.user.has_roles(user, models.UserRole.Doctor)
            and crud.user.get(db, patient_id).doctor_id == user.id
        )
        or (
            crud.user.has_roles(user, models.UserRole.Patient) and user.id == patient_id
        )
    )


def can_modify_results(db: Session, user: models.User, patient_id: Optional[UUID]):
    if patient_id is None:
        return crud.user.has_roles(user, models.UserRole.Admin)

    return crud.user.has_roles(user, models.UserRole.Admin) or (
        crud.user.has_roles(user, models.UserRole.Doctor)
        and crud.user.get(db, patient_id).doctor_id == user.id
    )


@router.post("/recordings/upload")
async def upload_audio_file(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    patient_id: UUID,
    file_in: UploadFile = File(...),
):

    if not can_modify_results(db, current_user, patient_id):
        raise HTTPException(
            status_code=403, detail="Insufficient privilages to access this patient"
        )
    data = await file_in.read()

    rec_create = RecordingCreate(
        blob=data, patient_id=patient_id, filename=file_in.filename
    )
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
    if not can_access_results(db, current_user, recording.patient_id):
        raise HTTPException(
            status_code=403, detail="Insufficient privilages to access this patient"
        )
    return dict(
        id=recording.id,
        filename=recording.filename,
        patient_id=recording.patient_id,
        byte_length=recording.byte_length,
    )


@router.get("/recordings")
def get_recordings(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    patient_id: Optional[UUID] = None,
    skip: int = 0,
    limit: int = 100,
):
    if not can_access_results(db, current_user, patient_id):
        raise HTTPException(
            status_code=403, detail="Insufficient privileges to access these recordings"
        )
    if patient_id is None:
        recordings = crud.recording.get_multi(db, skip, limit)
    else:
        recordings = crud.recording.get_by_patient_id(db, patient_id)
    recs = []
    for rec in recordings:
        recs.append(
            dict(
                id=rec.id,
                filename=rec.filename,
                creation_date=rec.creation_date,
                patient_id=rec.patient_id,
            )
        )
    return recs


@router.post("/recordings/{recording_id}/analyze", status_code=status.HTTP_202_ACCEPTED)
def perform_analysis(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    recording_id: UUID,
):
    db: Session
    for db in deps.get_db():
        recording = crud.recording.get(db, recording_id)
        if not can_modify_results(db, current_user, recording.patient_id):
            raise HTTPException(
                status_code=403,
                detail="Insufficient privilages to access this recording",
            )
        analysis_create = AnalysisResultCreate(
            status="CREATED", patient_id=recording.patient_id, recording_id=recording_id
        )
        result = crud.analysis_result.create(db, obj_in=analysis_create)
        celery_ref.send_file.delay(recording_id, result.id)
        return result.id


@router.get("/results/{analysis_id}")
def get_result_by_id(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    analysis_id: UUID,
):
    result = crud.analysis_result.get(db, analysis_id)
    if not can_access_results(db, current_user, result.patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privileges to access this analysis result",
        )
    return dict(id=result.id, status=result.status, patient_id=result.patient_id)


@router.get("/results/{analysis_id}/frames")
def get_result_frames(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    analysis_id: UUID,
):
    result = crud.analysis_result.get(db, analysis_id)
    if not can_access_results(db, current_user, result.patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privileges to access this analysis result",
        )
    if result.status != "COMPLETED":
        raise HTTPException(
            status_code=404,
            detail="The analysis with given ID has not been finished yet",
        )
    return result.frames


@router.get("/results/{analysis_id}/statistics")
def get_result_statistics(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    analysis_id: UUID,
):
    result = crud.analysis_result.get(db, analysis_id)
    if not can_access_results(db, current_user, result.patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privileges to access this analysis result",
        )
    if result.status != "COMPLETED":
        raise HTTPException(
            status_code=404,
            detail="The analysis with given ID has not been finished yet",
        )
    return result.statistics


@router.get("/results/{analysis_id}/status")
def get_result_status(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    analysis_id: UUID,
):
    result = crud.analysis_result.get(db, analysis_id)
    if not can_access_results(db, current_user, result.patient_id):
        raise HTTPException(
            status_code=403,
            detail="Insufficient privileges to access this analysis result",
        )
    return result.status


@router.get("/results")
def get_results(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    patient_id: UUID = None,
    skip: int = 0,
    limit: int = 100,
):
    if not crud.user.has_roles(
        current_user, models.UserRole.Admin, models.UserRole.Doctor
    ):
        raise HTTPException(
            status_code=403, detail="Insufficient privilages to access all results"
        )

    all_results = []

    def handle_admin():
        if patient_id is None:
            results = crud.analysis_result.get_multi(db, skip, limit)
        else:
            results = crud.analysis_result.get_by_patient_id(db, patient_id)
        return results

    def handle_doctor():
        results = []
        if patient_id is None:
            patients = crud.user.get_by_doctor_id(db, current_user.id)
            for pat in patients:
                results.extend(crud.analysis_result.get_by_patient_id(db, pat.id))
        else:
            if can_modify_results(db, current_user, patient_id):
                results = crud.analysis_result.get_by_patient_id(db, patient_id)
            else:
                raise HTTPException(
                    status_code=403,
                    detail="Insufficient privilages to access this patient's results",
                )
        return results

    if crud.user.has_roles(current_user, models.UserRole.Admin):
        all_results = handle_admin()
    else:
        all_results = handle_doctor()

    filtered_results = []
    for result in all_results:
        filtered_results.append(
            dict(
                id=result[0].id,
                status=result[0].status,
                patient_id=result[0].patient_id,
                created_date=result[0].created_date,
                recording_id=result[0].recording_id,
                recording_name=result[1].filename,
            )
        )
    return filtered_results
