import time
import os

from celery import Celery

celery = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis;//localhost:6379"),
)


@celery.task(name="analyze")
def perform_analysis(task_type):
    time.sleep(5)
    return True
