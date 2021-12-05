import uuid

from sqlalchemy import Boolean, Column, String, Integer, LargeBinary, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy_json import NestedMutableJson

from app.db.base_class import Base


class AnalysisResult(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    status = Column(String, nullable=False)
    error = Column(String, nullable=True)
    result = Column(Integer, nullable=True)
    frames = Column(NestedMutableJson, nullable=True)
    statistics = Column(NestedMutableJson, nullable=True)
