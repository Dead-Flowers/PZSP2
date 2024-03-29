from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.models.user import UserRole, Sex


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None
    pesel: Optional[str] = None
    passport_num: Optional[str] = None
    first_name: Optional[str] = None
    second_name: Optional[str] = None
    last_name: Optional[str] = None
    sex: Optional[Sex] = None
    birth_date: Optional[date] = None
    doctor_id: Optional[UUID] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str
    role: UserRole
    pesel: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
