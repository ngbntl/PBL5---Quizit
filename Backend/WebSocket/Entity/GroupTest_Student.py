from fastapi import WebSocket
from Backend.Model.DB_model import StudentTest, Student


class GroupTest_Student:
    STATE_DISCONNECTED = 'DISCONNECTED'
    STATE_READY = 'READY'
    STATE_WORKING = 'WORKING'
    STATE_BANNED = 'BANNED'
    STATE_SUBMIT = 'SUBMIT'

    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.student: Student = None
        self.room = None
        self.state = self.STATE_READY
        self.violate = 0
        self.student_test: StudentTest = None

    def set_room(self, room):  # room: Room_GroupTest
        self.room = room
        return self

    def get_room(self):  # -> Room_GroupTest
        return self.room

    def set_state(self, state: str):
        self.state = state
        return self

    def get_state(self) -> str:
        return self.state

    def increase_violate(self):
        self.violate += 1
        return self

    def get_violate(self):
        return self.violate

    def set_student(self, student):
        self.student = student
        return self

    def get_student(self):
        return self.student

    def get_student_test(self):
        return self.student_test

    def set_student_test(self, student_test):
        self.student_test = student_test
        return self

    def serialize(self, include: set):
        ser = dict()
        if 'student' in include:
            ser['student'] = self.student.serialize({'id', 'name', 'email', 'avatar_path'})
        if 'violate' in include:
            ser['violate'] = self.violate
        if 'state' in include:
            ser['state'] = self.state
        if 'score' in include:
            ser['score'] = self.student_test.score

        return ser

    def get_score(self):
        return self.student_test.score

    # def submit(self, student_answer: list[list[int]]):
    #     student_test = self.room.submit(self.student.id, student_answer)
    #     self.set_student_test(student_test)