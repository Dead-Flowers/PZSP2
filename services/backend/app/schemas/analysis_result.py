from typing import Optional
from uuid import UUID
from app.services.bowel_service import BowelAnalysisResult

from fastapi import UploadFile
from pydantic import BaseModel, validator


class AnalysisResultBase(BaseModel):
    pass


class AnalysisResultCreate(AnalysisResultBase):
    get_status_return_value: BowelAnalysisResult

    class Config:
        arbitrary_types_allowed = True

    @validator("get_status_return_value")
    def status_return_validator(cls, v, values, **kwargs):
        return v
