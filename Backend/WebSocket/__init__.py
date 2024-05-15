import asyncio
import json
from typing import Annotated

from fastapi import WebSocket, Header
from starlette.websockets import WebSocketDisconnect

from Backend.Business.BO_authenticate import get_current_user
from Backend.Model.DB_model import Student
from Backend.Router import app
from Backend.WebSocket.Room_GroupTest import Room_GroupTest


class ClientMessage:
    JOIN_GROUP_TEST = "JOIN GROUP TEST"

    def __init__(self, data: dict):
        self.command = data.get('command')
        self.detail = data.get('detail')

class ConnectionManager:
    def __init__(self):
        self.active_connections: set[WebSocket] = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        if self.active_connections:
            await asyncio.gather(*[connection.send_text(message) for connection in self.active_connections])


student_ws_manager = ConnectionManager()
room_group_test: set[Room_GroupTest] = ()

@app.websocket("/student")
async def student_ws_endpoint(token: Annotated[str, Header()], websocket: WebSocket):
    student = await get_current_user(token=token)
    if student is None or not isinstance(student, Student):
        raise WebSocketDisconnect()
    await student_ws_manager.connect(websocket)
    try:
        while True:
            msg = ClientMessage(json.loads((await websocket.receive_text())))
            if msg.command == ClientMessage.JOIN_GROUP_TEST:
                group_test_id = msg.detail['group_test_id']
                for group_test in room_group_test:
                    if group_test.id == group_test_id:
                        group_test.students.append(student)
                        break

    except WebSocketDisconnect:
        student_ws_manager.disconnect(websocket)