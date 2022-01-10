import app
from fastapi import status, Depends, WebSocket
from app.services.ws_manager import manager as ws_manager
from app.api import deps
from sqlalchemy.orm import Session


async def handle_websocket(websocket: WebSocket):
    async def handle_auth():
        auth = await websocket.receive_json()
        if not auth or "type" not in auth or "payload" not in auth:
            raise RuntimeError()
        for db in deps.get_db():
            return deps.get_current_user(db, auth["payload"])

    async def handle_data():
        data = await websocket.receive_json()

    await websocket.accept()
    try:
        user = await handle_auth()
        await ws_manager.connect(websocket, user)
        await websocket.send_json(dict(user=user.email))
        while True:
            await handle_data()
    finally:
        ws_manager.disconnect(websocket)
