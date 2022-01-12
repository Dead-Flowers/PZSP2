from uuid import UUID
from typing import List

from app.crud.base import CRUDBase
from app.schemas.news import NewsCreate, NewsUpdate

from sqlalchemy.orm import Session
from app.models.news import News


class CRUDNews(CRUDBase[News, NewsCreate, NewsUpdate, None]):
    def get_last_news(self, db: Session, count: int = 5) -> List[News]:
        return db.query(News).limit(count).order_by(News.creation_date.desc()).all()

    def create(self, db: Session, *, obj_in: NewsCreate) -> News:
        db_obj = News(title=obj_in.title, description=obj_in.description)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: News, obj_in: NewsUpdate) -> News:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def remove(self, db: Session, news_id: UUID) -> None:
        db.query(News).filter(News.id == news_id).delete()


news = CRUDNews(News)
