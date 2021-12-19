from typing import Optional
from uuid import UUID

from fastapi import UploadFile
from pydantic import BaseModel


class RecordingBase(BaseModel):
    pass


class RecordingCreate(RecordingBase):
    blob: bytes
    filename: str
    patient_id: UUID
