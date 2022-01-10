import json

from app.models.result import AnalysisResult


class WebsocketMessage:
    TYPE = "unknown"

    def __init__(self, type, **kwargs) -> None:
        self.type = type
        self.payload = kwargs

    def to_json(self):
        return json.dumps(dict(type=self.type, payload=self.payload), default=vars)


class AnalysisStateUpdated(WebsocketMessage):
    TYPE = "analysis-state-updated"

    def __init__(self, id: str, status: str) -> None:
        super().__init__(self.TYPE, id=id, status=status)
