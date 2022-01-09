import celery
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api import api_router
from app.core.config import settings
from app.api.endpoints.websocket import handle_websocket
from app.services.celery_monitor import monitor
from app.worker.app import celery as celery_app

__version__ = "0.1.0"

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.on_event('startup')
def startup():
    monitor.start(celery_app)

@app.get("/")
def home():
    return {"msg": "Hello World"}


app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_websocket_route("/ws", handle_websocket)