from typing import List
from uuid import UUID
from datetime import datetime
from app.models.systemexception import SystemException


class RecordingResponse:
    id: UUID
    filename: str
    patient_id: UUID
    byte_length: int


class RecordingPatientResponse:
    id: UUID
    filename: str
    patient_id: UUID
    byte_length: int


class AnalysisResponse:
    id: UUID
    status: str
    patient_id: UUID
    recording_id: UUID


class AnalysisStatsResponse:
    success: int
    failure: int
    exceptions: List[SystemException]


class AnalysisResultResponse:
    id: UUID
    status: str
    patient_id: UUID
    created_date: datetime
    recording_id: UUID
    recording_name: str
