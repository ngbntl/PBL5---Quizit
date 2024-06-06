from fastapi import WebSocket
from Backend.Model.DB_model import Student


class StudentWS:
    def __init__(self, websocket: WebSocket, student: Student):
        self.websocket = websocket
        self.student = student

    async def send_text(self, text: str):
        await self.websocket.send_text(text)

    async def send_json(self, data: dict):
        await self.websocket.send_json(data)

    async def receive_json(self):
        return await self.websocket.receive_json()