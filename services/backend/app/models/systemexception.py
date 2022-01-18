from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base_class import Base
import datetime


class SystemException(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    source = Column(String, index=True)
    value = Column(String, nullable=True)
    creation_date = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
