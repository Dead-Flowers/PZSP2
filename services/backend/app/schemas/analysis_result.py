from typing import Dict, Optional
from uuid import UUID

from sqlalchemy.sql.sqltypes import String, Integer
from sqlalchemy_json import NestedMutableJson
from app.services.bowel_service import BowelAnalysisResult

from fastapi import UploadFile
from pydantic import BaseModel, validator


class AnalysisResultBase(BaseModel):
    pass


class AnalysisResultCreate(AnalysisResultBase):
    status: str


class AnalysisResultStatusUpdate(AnalysisResultBase):
    status: str


class AnalysisResultUpdate(AnalysisResultBase):
    status: str
    error: str
    result: int
    frames: list
    statistics: dict

    class Config:
        arbitrary_types_allowed = True

    @validator("frames")
    def status_return_validator(cls, v, values, **kwargs):
        return v
