from typing import List, Optional
from uuid import UUID
from datetime import datetime
from app.schemas.systemexception import SystemException
from pydantic import BaseModel


class RecordingResponse(BaseModel):
    id: Optional[UUID] = None
    filename: str
    creation_date: Optional[datetime]
    patient_id: Optional[UUID]


class RecordingPatientResponse(BaseModel):
    id: Optional[UUID] = None
    filename: str
    patient_id: Optional[UUID] = None
    byte_length: Optional[int]


class AnalysisResponse(BaseModel):
    id: Optional[UUID] = None
    status: str
    patient_id: Optional[UUID] = None
    recording_id: Optional[UUID] = None


class AnalysisStatsResponse(BaseModel):
    success: int
    failure: int
    exceptions: List[SystemException]


class AnalysisResultResponse(BaseModel):
    id: Optional[UUID] = None
    status: str
    patient_id: Optional[UUID] = None
    created_date: Optional[datetime]
    recording_id: Optional[UUID] = None
    recording_name: str
