import enum
import uuid

from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserRole(enum.Enum):
    Admin = "admin"
    Doctor = "doctor"
    Patient = "patient"


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    first_name = Column(String, index=True)
    second_name = Column(String, index=True)
    last_name = Column(String, index=True)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), default=None)

    doctor = relationship("User", remote_side=[id])
