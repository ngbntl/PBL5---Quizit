from fastapi import WebSocket
from Backend.WebSocket.Business.BO_Student_Message import BO_Student_Message


async def student_ws_endpoint(websocket: WebSocket):
    await BO_Student_Message(websocket).handle()
