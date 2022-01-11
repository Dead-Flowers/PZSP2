import enum
import uuid

from sqlalchemy import Column, Date, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserRole(enum.Enum):
    Admin = "admin"
    Doctor = "doctor"
    Patient = "patient"


class Sex(enum.Enum):
    Male = "male"
    Female = "female"
    Other = "other"


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    pesel = Column(String(11), index=True)
    passport_num = Column(String, index=True)
    first_name = Column(String, index=True)
    second_name = Column(String, index=True)
    last_name = Column(String, index=True)
    sex = Column(Enum(Sex))
    birth_date = Column(Date)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), default=None)

    doctor = relationship("User", remote_side=[id])
