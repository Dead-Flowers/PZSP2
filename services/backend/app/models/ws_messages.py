import json

class WebsocketMessage:
    TYPE = 'unknown'
    def __init__(self, **kwargs) -> None:
        self.type = type
        self.payload = kwargs
    
    def to_json(self):
        return json.dumps(dict(type=self.type, payload=self.payload), default=vars)

class AnalysisStateUpdated(WebsocketMessage):
    TYPE = __name__
    def __init__(self, analysis_id: str) -> None:
        super().__init__(self.TYPE, analysis_id=analysis_id)