from sqlite3 import Date
from typing import Optional
from uuid import UUID
from pydantic.main import BaseModel
from datetime import datetime


class NewsBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class NewsCreate(NewsBase):
    pass


class NewsUpdate(NewsBase):
    pass


class NewsInDBBase(NewsBase):
    id: Optional[UUID] = None
    creation_date: Optional[datetime]

    class Config:
        orm_mode = True


class News(NewsInDBBase):
    pass
