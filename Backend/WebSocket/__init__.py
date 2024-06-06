import json
import random
from collections import defaultdict
from datetime import datetime
from typing import Annotated
from fastapi import WebSocket, Header
from starlette.websockets import WebSocketDisconnect

from Backend.Business import bcrypt_context
from Backend.Business.BO_WebSocket import BO_WebSocket
from Backend.Business.BO_authenticate import get_current_user

from Backend.Model.DB_model import Student, Teacher, GroupTest, StudentTest, Test, Question, StudentWork_Question
from Backend.Router import app
from Backend.WebSocket.StudentWS import StudentWS

bo_websocket = BO_WebSocket()


class ClientMessage:
    AUTHENTICATE = 'AUTHENTICATE'
    JOIN_GROUP_TEST = 'JOIN GROUP TEST'
    GET_TEST = 'GET TEST'
    SUBMIT_TEST = 'SUBMIT TEST'

    def __init__(self, data: dict):
        self.command = data.get('command')
        self.detail = data.get('detail')


class Room_GroupTest:
    def __init__(self, group_test_id: str):
        self.group_test_id = group_test_id
        self.teacher = None
        self.students: dict[str, (StudentWS, StudentTest)] = dict()
        self._group_test: GroupTest = None
        self._test: Test = None
        self._questions: defaultdict[int, list[Question]] = None

    @property
    def group_test(self):
        if self._group_test is None:
            self._group_test = bo_websocket.get_group_test_by_id(self.group_test_id)
        return self._group_test

    @property
    def hash_pswd(self):
        return self.group_test.hash_pswd

    @hash_pswd.setter
    def hash_pswd(self, value):
        self.group_test.hash_pswd = value

    @property
    def questions(self):
        if self._questions is None:
            questions = bo_websocket.get_all_questions_in_test(self.group_test.test_id)
            self._questions = defaultdict(list)
            for q in questions:
                self._questions[q.difficulty].append(q)
        return self._questions

    @property
    def test(self):
        if self._test is None:
            self._test = bo_websocket.get_test_by_id(self.group_test.test_id)
        return self._test

    def add_student_ws(self, student_ws: StudentWS):
        self.students[student_ws.student.id] = (student_ws, None)

    def get_student_test(self, student_id: str) -> StudentTest:
        if student_id in self.students.keys():  # check if student is in room
            _, student_test = self.students[student_id]
            if student_test is None:
                return self.generate_student_test(student_id)
            return student_test
        return None

    def generate_student_work_question(self) -> list[StudentWork_Question]:
        ans = list()
        for ts in self.test.structure:
            for noq in ts.number_of_question:
                num_question = max(noq.number_of_question, len(self.questions[noq.difficulty]))
                for q in random.sample(self.questions[noq.difficulty], num_question):
                    ans.append(StudentWork_Question(content=q.content, answer=q.answer, attachment=q.attachment, student_answer=[]))
        return ans

    def generate_student_test(self, student_id: str) -> StudentTest:
        student_ws, student_test = self.students[student_id]
        if student_test is not None:
            return student_test
        student_test = StudentTest(student_id=student_id, group_test_id=self.group_test_id, start=datetime.now(), student_work=self.generate_student_work_question(), score=0)
        # bo_websocket.insert_student_test(student_test)
        self.students[student_id] = (student_ws, student_test)
        return student_test


room_group_test: dict[Room_GroupTest] = dict()


@app.websocket("/student")
async def student_ws_endpoint(websocket: WebSocket):
    student = None
    # if student is None or not isinstance(student, Student):
    #     raise WebSocketDisconnect()

    student_ws = StudentWS(websocket, student)
    room = None
    try:
        await websocket.accept()
        while True:
            try:
                msg = ClientMessage(json.loads((await websocket.receive_text())))
                if msg.command == ClientMessage.AUTHENTICATE:
                    student = get_current_user(msg.detail['token'])
                    if student is None or not isinstance(student, Student):
                        await student_ws.send_text('Invalid token')
                        continue
                    student_ws.student = student
                    await student_ws.send_text('Authenticated')

                elif msg.command == ClientMessage.JOIN_GROUP_TEST:
                    if student is None:
                        await student_ws.send_text('You have not authenticated')
                        continue
                    group_test_id = msg.detail['group_test_id']
                    password = msg.detail['password']
                    room = Room_GroupTest(group_test_id)  # get the room

                    if group_test_id not in room_group_test.keys():  # room not exist
                        if room.group_test is None:  # check if group test is exist
                            room = None
                            await student_ws.send_text('Group test not found')
                            continue
                        if room.group_test.is_active() is False:
                            room = None
                            await student_ws.send_text('Group test is not active')
                            continue
                        room_group_test[group_test_id] = room  # add room to dict

                    if room.hash_pswd != room_group_test[group_test_id].hash_pswd:  # check if password is changed
                        room_group_test[group_test_id].hash_pswd = room.hash_pswd  # update password

                    if bo_websocket.check_student_in_group(room.group_test.group_id, student.id) is False:  # check if student is in group
                        room = None
                        await student_ws.send_text('You are not in this group')
                        continue

                    if bcrypt_context.verify(password, room.hash_pswd):  # check password
                        room.add_student_ws(student_ws)  # add student to room
                        await student_ws.send_text('Joined group test')
                    else:
                        await student_ws.send_text('Wrong password')
                        continue

                elif msg.command == ClientMessage.GET_TEST:  # Add more command here
                    if student is None:
                        await student_ws.send_text('You have not authenticated')
                        continue
                    if room is None:
                        await student_ws.send_text('You have not joined any group')
                        continue

                    student_test = room.get_student_test(student.id)

                    # resp['start'] = resp['start'].isoformat() if resp['start'] is not None else None
                    # resp['end'] = resp['end'].isoformat() if resp['end'] is not None else None
                    await student_ws.send_json(student_test.serialize())

                elif msg.command == ClientMessage.SUBMIT_TEST:
                    if student is None:
                        await student_ws.send_text('You have not authenticated')
                        continue
                    if room is None:
                        await student_ws.send_text('You have not joined any group')
                        continue


            except WebSocketDisconnect:
                if room is not None:
                    room.students.pop(student.id)
                break
            finally:
                pass

    except WebSocketDisconnect:
        pass


@app.websocket("/teacher")
async def teacher_ws_endpoint(websocket: WebSocket):
    pass