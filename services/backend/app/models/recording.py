import uuid

from sqlalchemy import Boolean, Column, String, Integer, LargeBinary, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.base_class import Base


class Recording(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    filename = Column(String, index=True)
    byte_length = Column(Integer, nullable=False)
    blob = Column(LargeBinary, nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
