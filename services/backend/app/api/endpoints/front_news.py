from typing import Any, List
from uuid import UUID

from sqlalchemy.orm import Session
from app import crud, models
from app.api import deps
from app import crud, models, schemas
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import News

router = APIRouter()


@router.post("/", response_model=News)
async def add_news(
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


@router.get("/", response_model=List[News])
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


@router.get("/{news_id}", response_model=News)
async def get_news_by_id(*, db: Session = Depends(deps.get_db), news_id: UUID):
    result = crud.news.get(db, news_id)
    return result


@router.put("/{news_id}", response_model=News)
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


@router.delete("/{news_id}")
async def remove_news(
    *,
    db: Session = Depends(deps.get_db),
    news_id: UUID,
    current_user: models.User = Depends(deps.get_current_user)
) -> Any:
    if not crud.user.has_roles(current_user, models.UserRole.Admin):
        raise HTTPException(
            status_code=403, detail="Insufficient privileges to create news"
        )
    crud.news.remove(db, news_id)
