import uuid
import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class News(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    creation_date = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
