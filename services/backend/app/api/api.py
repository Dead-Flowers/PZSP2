from fastapi import APIRouter

from app.api.endpoints import users
from app.api.endpoints import analysis

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
