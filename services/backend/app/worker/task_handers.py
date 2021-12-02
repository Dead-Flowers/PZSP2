from app.schemas.analysis_result import AnalysisResultCreate
from celery.signals import after_task_publish, task_success, task_postrun
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger
from app.api import deps
from app import crud
