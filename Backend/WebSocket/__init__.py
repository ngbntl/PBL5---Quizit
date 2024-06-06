from fastapi import WebSocket

from Backend.WebSocket.Business.BO_Room_GroupTest import BO_Room_GroupTest
from Backend.WebSocket.Endpoint.student_ws_endpoint import student_ws_endpoint
from Backend.WebSocket.Endpoint.teacher_ws_endpoint import teacher_ws_endpoint
from Backend.Router import app
from Backend.WebSocket.Entity.StudentWS import StudentWS
from Backend.WebSocket.Entity.TeacherWS import TeacherWS


@app.websocket("/student")
async def student_endpoint(websocket: WebSocket):
    await student_ws_endpoint(websocket)


@app.websocket("/teacher")
async def teacher_endpoint(websocket: WebSocket):
    await teacher_ws_endpoint(websocket)