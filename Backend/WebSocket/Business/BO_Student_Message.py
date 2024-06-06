from fastapi import WebSocket
from starlette import status
from starlette.websockets import WebSocketDisconnect

from Backend.Business import bcrypt_context
from Backend.WebSocket.Entity.ClientMessage import ClientMessage
from Backend.WebSocket.Entity.ResponseMessage import ResponseMessage
from Backend.WebSocket.Entity.Room_GroupTest import Room_GroupTest
from Backend.WebSocket.Entity.StudentWS import StudentWS
from Backend.WebSocket.Business.BO_WebSocket import BO_WebSocket
from Backend.WebSocket.Business.BO_Room_GroupTest import BO_Room_GroupTest
from Backend.Model.DB_model import Student
from Backend.Business.BO_authenticate import get_current_user


class BO_Student_Message:
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.student = None
        self.room = None
        self.bo_websocket = None
        self.bo_room_grouptest = None
        self.message = None
        self.response = None
        self.student_ws = None

    async def handle(self):
        try:
            await self.websocket.accept()
            self.bo_websocket = BO_WebSocket()
            self.bo_room_grouptest = BO_Room_GroupTest()
            self.message = ClientMessage()
            self.response = ResponseMessage()
            self.student_ws = StudentWS(self.websocket, None)

            while True:
                try:
                    msg = self.message.set_message(**await self.websocket.receive_json())
                    if msg.command == ClientMessage.AUTHENTICATE:
                        self.student = await get_current_user(msg.detail['token'])
                        if self.student is None or not isinstance(self.student, Student):
                            self.student = None
                            await self.websocket.send_json(self.response.set_status(status.HTTP_401_UNAUTHORIZED).set_message('Invalid token').serialize())
                            continue

                        self.student_ws.student = self.student
                        await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('Authenticated').serialize())
                        continue

                    if self.student is None:
                        await self.websocket.send_json(self.response.set_status(status.HTTP_401_UNAUTHORIZED).set_message('You have not authenticated').serialize())
                        continue

                    if msg.command == ClientMessage.JOIN_GROUP_TEST:
                        group_test_id = msg.detail['group_test_id']
                        password = msg.detail['password']
                        self.room = Room_GroupTest(group_test_id)  # create the room

                        if self.room.is_exist() is False:  # check if group test is exist
                            self.room = None
                            await self.websocket.send_json(self.response.set_status(status.HTTP_404_NOT_FOUND).set_message('Group test not found').serialize())
                            continue

                        if self.bo_room_grouptest.is_room_exist(group_test_id) is False:  # room not exist in manager
                            if self.room.is_active() is False:
                                self.room = None
                                await self.websocket.send_json(self.response.set_status(status.HTTP_404_NOT_FOUND).set_message('Group test is not active').serialize())
                                continue

                            self.bo_room_grouptest.add_room(group_test_id, self.room)  # add room to manager

                        if self.room.hash_pswd != self.bo_room_grouptest.get_room_hash_password(group_test_id):  # check if password is changed
                            self.bo_room_grouptest.set_room_hash_password(group_test_id, self.room.hash_pswd)  # update password

                        if self.bo_websocket.check_student_in_group(self.room.group_test.group_id, self.student.id) is False:  # check if student is in group
                            self.room = None
                            await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message('You are not in this group').serialize())
                            continue

                        if bcrypt_context.verify(password, self.room.hash_pswd):  # check password
                            self.room.add_student_ws(self.student_ws)  # add student to room
                            await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('Joined group test').serialize())
                            continue
                        else:
                            await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message('Group test password is wrong').serialize())
                            continue
                    if self.room is None:
                        await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message('You have not joined any group').serialize())
                        continue

                    if msg.command == ClientMessage.GET_TEST:  # Add more command here

                        student_test = self.room.get_student_test(self.student.id)
                        await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message(student_test.serialize()).serialize())

                    elif msg.command == ClientMessage.SUBMIT_TEST:
                        pass


                except WebSocketDisconnect:
                    # if room is not None:
                    #     room.students.pop(student.id)
                    break

        except WebSocketDisconnect:
            pass
