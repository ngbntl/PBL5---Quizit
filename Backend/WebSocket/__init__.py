import json
from typing import Annotated
from fastapi import WebSocket, Header
from starlette.websockets import WebSocketDisconnect

from Backend.Business.BO_authenticate import get_current_user
from Backend.Business.BO_group import BO_group
from Backend.Business.BO_group_student import BO_group_student
from Backend.Business.BO_group_test import BO_group_test
from Backend.Model.DB_model import Student, Teacher, GroupTest, StudentTest
from Backend.Router import app


class BO_WebSocket:
    def __init__(self):
        self._bo_group_test = None
        self._bo_group = None
        self._bo_group_student = None

    @property
    def bo_group_test(self):
        if self._bo_group_test is None:
            self._bo_group_test = BO_group_test()
        return self._bo_group_test

    @property
    def bo_group(self):
        if self._bo_group is None:
            self._bo_group = BO_group()
        return self._bo_group

    @property
    def bo_group_student(self):
        if self._bo_group_student is None:
            self._bo_group_student = BO_group_student()
        return self._bo_group_student

    def get_group_test_by_id(self, group_test_id: str) -> GroupTest:
        return self.bo_group_test.get_group_test_by_id(group_test_id)

    def check_student_in_group(self, group_id: str, student_id: str) -> bool:
        return self.bo_group_student.check_student_in_group(group_id, student_id)


bo_websocket = BO_WebSocket()


class ClientMessage:
    JOIN_GROUP_TEST = 'JOIN GROUP TEST'
    GET_TEST = 'GET TEST'
    SUBMIT_TEST = 'SUBMIT TEST'

    def __init__(self, data: dict):
        self.command = data.get('command')
        self.detail = data.get('detail')


class StudentWS:
    def __init__(self, websocket: WebSocket, student: Student):
        self.websocket = websocket
        self.student = student

    async def send_text(self, text: str):
        await self.websocket.send_text(text)

    async def send_json(self, data: dict):
        await self.websocket.send_json(data)


class Room_GroupTest:
    def __init__(self, id: str):
        self.group_test: GroupTest = bo_websocket.get_group_test_by_id(id)
        self.teacher = None
        self.students: dict[str, (StudentWS, StudentTest)] = dict()

    def add_student_ws(self, student_ws: StudentWS):
        self.students[student_ws.student.id] = (student_ws, None)

    def get_student_work(self, student_id: str) -> StudentTest:
        pass


room_group_test: dict[Room_GroupTest] = dict()


@app.websocket("/student")
async def student_ws_endpoint(token: Annotated[str, Header()], websocket: WebSocket):
    student = await get_current_user(token=token)
    if student is None or not isinstance(student, Student):
        raise WebSocketDisconnect()

    student_ws = StudentWS(websocket, student)
    room = None
    try:
        await websocket.accept()
        while True:
            try:
                msg = ClientMessage(json.loads((await websocket.receive_text())))

                if msg.command == ClientMessage.JOIN_GROUP_TEST:
                    group_test_id = msg.detail['group_test_id']
                    if group_test_id not in room_group_test.keys():  # room not exist
                        room = Room_GroupTest(group_test_id)  # create new room
                        if room.group_test is None:  # check if group test is exist
                            room = None
                            await student_ws.send_text('Group test not found')
                            continue
                        if room.group_test.is_active() is False:
                            room = None
                            await student_ws.send_text('Group test is not active')
                            continue
                        room_group_test[group_test_id] = room  # add room to dict

                    if bo_websocket.check_student_in_group(room.group_test.group_id,
                                                           student.id) is False:  # check if student is in group
                        room = None
                        await student_ws.send_text('You are not in this group')
                        continue

                    room.add_student_ws(student_ws)  # add student to room
                    await student_ws.send_text('Joined group test')

                elif msg.command == ClientMessage.GET_TEST:  # Add more command here
                    student_work = room.get_student_work(student.id)
                    await student_ws.send_json(student_work.jsonify())
                elif msg.command == ClientMessage.SUBMIT_TEST:
                    pass
            except WebSocketDisconnect:
                if room is not None:
                    room.students.pop(student.id)
                break
            finally:
                pass

    except WebSocketDisconnect:
        pass
