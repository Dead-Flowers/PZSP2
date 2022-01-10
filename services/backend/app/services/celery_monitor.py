import threading
import time

from celery.events import EventReceiver
from kombu import Connection as BrokerConnection

from celery.events.state import State
from sqlalchemy.sql.functions import AnsiFunction

from app.api import deps
from app.models.ws_messages import AnalysisStateUpdated
from app.services.notification_service import notificationService
from app.services.ws_manager import manager
import asyncio


class CeleryMonitor(object):
    def __init__(self):
        self._state = State()

    @property
    def state(self) -> State:
        return self._state

    def start(self, celery_app):
        if hasattr(self, "thread"):
            return
        self.celery_app = celery_app
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()

    def handle_analysis(self, event):
        state = event["state"]
        analysis_id = event["analysis_id"]
        recipients = []
        for db in deps.get_db():
            recipients = notificationService.get_analysis_update_recipients(
                db, analysis_id
            )
        broadcast_task = manager.broadcast(
            recipients, AnalysisStateUpdated(analysis_id, state).to_json()
        )
        asyncio.get_event_loop().run_until_complete(broadcast_task)

    def catchall(self, event):
        try:
            event_type = event["type"]
            if event_type == "worker-heartbeat":
                return
            if event_type == "task-analysis-status":
                return self.handle_analysis(event)

            self._state.event(event)
        except Exception as e:
            print(e)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while True:
            try:
                with self.celery_app.connection() as connection:
                    recv = self.celery_app.events.Receiver(
                        connection, handlers={"*": self.catchall}
                    )
                    recv.capture(limit=None, timeout=None, wakeup=True)

            except (InterruptedError, SystemExit):
                break
            except Exception:
                # unable to capture
                pass


monitor = CeleryMonitor()
