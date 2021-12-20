from typing import Any, List
from uuid import UUID

from sqlalchemy.sql.sqltypes import String

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    pesel: str = "",
    pass_num: str = "",
    first_name: str = "",
    second_name: str = "",
    last_name: str = "",
    email: str = "",
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    if crud.user.has_roles(current_user, models.UserRole.Admin):
        # return crud.user.get_multi(db, skip=skip, limit=limit)
        return crud.user.get_by_params(
            db,
            pesel,
            pass_num,
            first_name,
            second_name,
            last_name,
            email,
            current_user,
            skip,
            limit,
        )
    elif crud.user.has_roles(current_user, models.UserRole.Doctor):
        # return crud.user.get_assigned_patients(db, current_user, skip=skip, limit=limit)
        return crud.user.get_by_params(
            db,
            pesel,
            pass_num,
            first_name,
            second_name,
            last_name,
            email,
            current_user,
            skip,
            limit,
        )
    else:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.user_with_roles(models.UserRole.Admin)),
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    user = crud.user.create(db, obj_in=user_in)
    return user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    email: EmailStr = Body(None),
    password: str = Body(None),
    first_name: str = Body(None),
    second_name: str = Body(None),
    last_name: str = Body(None),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if first_name is not None:
        user_in.first_name = first_name
    if second_name is not None:
        user_in.second_name = second_name
    if last_name is not None:
        user_in.last_name = last_name
    if email is not None:
        user_in.email = email
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password, email=email, full_name=full_name)
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: UUID,
    current_user: models.User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if user == current_user:
        return user
    # TODO:  check if this doctor has the patient
   ''' if not crud.user.has_roles(
        current_user, models.UserRole.Admin, models.UserRole.Doctor
    ):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
        '''
    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: UUID,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.user_with_roles(models.UserRole.Admin)),
) -> Any:
    """
    Update a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user
