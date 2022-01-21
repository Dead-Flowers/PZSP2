from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict

from app.models.user import User
from app.schemas.user import UserInDB


class ConnectionManager:
    def __init__(self):
        self.connections_by_user: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, user: User):
        self.connections_by_user.setdefault(user.id, []).append(websocket)
        websocket.state.user_id = user.id

    async def disconnect(self, websocket: WebSocket):
        state = websocket.state
        if hasattr(state, "user_id"):
            self.connections_by_user[state.user_id].remove(websocket)
        await websocket.close()

    async def broadcast(self, user_ids: List[str], message: str):
        for user_id in user_ids:
            connections = self.connections_by_user.get(user_id, [])
            for connection in connections:
                await connection.send_text(message)

    async def broadcast_all(self, message: str):
        for (*_, connections) in self.connections_by_user.items():
            for connection in connections:
                await connection.send_text(message)


manager = ConnectionManager()
