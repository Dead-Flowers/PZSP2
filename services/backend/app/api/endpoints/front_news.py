from typing import Any
from uuid import UUID

from sqlalchemy.orm import Session
from app import crud, models
from app.schemas.recording import RecordingCreate
from app.worker import app as celery_ref
from app.api import deps
from starlette.responses import Response
from app import crud, models, schemas

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    File,
    UploadFile,
)

router = APIRouter()


@router.post("/")
async def add_frontpage_news(
    *,
    db: Session = Depends(deps.get_db),
    news_in: schemas.NewsCreate,
    current_user: models.User = Depends(deps.get_current_user)
) -> Any:
    if not crud.user.has_roles(current_user, models.UserRole.Admin):
        raise HTTPException(
            status_code=403, detail="Insufficient privileges to create news"
        )
    news = crud.news.create(db, obj_in=news_in)
    return news


@router.get("/")
async def get_news(*, db: Session = Depends(deps.get_db), count: int = 5) -> Any:
    results = crud.news.get_last_news(db, count)
    final = []
    for res in results:
        final.append(
            dict(
                id=res.id,
                title=res.title,
                description=res.description,
                creation_date=res.creation_date,
            )
        )
    return final


@router.put("/{news_id}")
async def update_news(
    *,
    db: Session = Depends(deps.get_db),
    news_id: UUID,
    news_in: schemas.NewsUpdate,
    current_user: models.User = Depends(deps.get_current_user)
) -> Any:
    if not crud.user.has_roles(current_user, models.UserRole.Admin):
        raise HTTPException(
            status_code=403, detail="Insufficient privileges to create news"
        )
    old_news = crud.news.get(db, news_id)
    news = crud.news.update(db, db_obj=old_news, obj_in=news_in)
    return news
