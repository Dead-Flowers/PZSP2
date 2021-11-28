from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException, File, UploadFile

from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.schemas.recording import RecordingCreate


router = APIRouter()
from app.api import deps


@router.post("/upload")
async def perform_analysis(
    *, db: Session = Depends(deps.get_db), file_in: UploadFile = File(...)
):
    data = await file_in.read()
    rec_create = RecordingCreate(blob=data, filename=file_in.filename)
    recording = crud.recording.create(db, obj_in=rec_create)
    return recording.id


@router.get("/{recording_id}")
def get_recording(
    *,
    db: Session = Depends(deps.get_db),
    recording_id: UUID,
) -> Any:
    recording = crud.recording.get(db, recording_id)
    return recording.filename
