from fastapi import APIRouter

from app.api.endpoints import analysis, front_news
from app.api.endpoints import users, login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
api_router.include_router(front_news.router, prefix="/news", tags=["news"])
