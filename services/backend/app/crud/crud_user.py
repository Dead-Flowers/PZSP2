from typing import Any, Dict, List, Optional, Union
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, or_

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User, UserRole
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_params(
        self,
        db: Session,
        user: User,
        pesel: str = "",
        pass_num: str = "",
        f_name: str = "",
        s_name: str = "",
        l_name: str = "",
        email: str = "",
        skip: int = 0,
        limit: int = 100,
    ) -> List[User]:
        params = [
            prop.ilike(f"%{val}%")
            for val, prop in zip(
                [pesel, pass_num, f_name, s_name, l_name, email],
                [
                    User.pesel,
                    User.passport_num,
                    User.first_name,
                    User.second_name,
                    User.last_name,
                    User.email,
                ],
            )
            if val
        ]
        if self.has_roles(user, UserRole.Admin):
            return db.query(User).filter(*params).offset(skip).limit(limit).all()
        else:
            return (
                db.query(User)
                .filter(*params)
                .filter(User.doctor_id == user.id)
                .offset(skip)
                .limit(limit)
                .all()
            )

    def get_by_doctor_id(self, db: Session, doctor_id: UUID) -> List[User]:
        return db.query(User).filter(User.doctor_id == doctor_id).all()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            role=obj_in.role,
            first_name=obj_in.first_name,
            second_name=obj_in.second_name,
            last_name=obj_in.last_name,
            doctor_id=obj_in.doctor_id,
            pesel=obj_in.pesel,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password", None):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def has_roles(self, user: User, *roles: UserRole) -> bool:
        return user.role in roles

    def get_assigned_patients(
        self, db: Session, doctor: User, *, skip: int = 0, limit: int = 100
    ):
        return (
            db.query(User)
            .filter(User.doctor_id == doctor.id)
            .offset(skip)
            .limit(limit)
            .all()
        )


user = CRUDUser(User)
