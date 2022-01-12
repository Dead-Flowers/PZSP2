from uuid import UUID
from pydantic import BaseModel


class RecordingBase(BaseModel):
    pass


class RecordingCreate(RecordingBase):
    blob: bytes
    filename: str
    patient_id: UUID
