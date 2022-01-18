from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class SystemExceptionBase(BaseModel):
    source: Optional[str] = None
    value: Optional[str] = None


class SystemExceptionCreate(SystemExceptionBase):
    pass


class SystemExceptionInDBBase(SystemExceptionBase):
    id: Optional[UUID] = None
    creation_date: Optional[datetime]

    class Config:
        orm_mode = True


class SystemException(SystemExceptionInDBBase):
    pass
