import random
from collections import defaultdict
from datetime import datetime

from Backend.Model.DB_model import StudentTest, GroupTest, Test, Question, StudentWork_Question
from Backend.WebSocket.Business.BO_WebSocket import BO_WebSocket
from Backend.WebSocket.Entity.StudentWS import StudentWS


class Room_GroupTest:
    def __init__(self, group_test_id: str):
        self.group_test_id = group_test_id
        self.teacher = None
        self.students: dict[str, (StudentWS, StudentTest)] = dict()
        self._group_test: GroupTest = None
        self._test: Test = None
        self._questions: defaultdict[int, list[Question]] = None
        self._bo_websocket = None

    @property
    def bo_websocket(self):
        if self._bo_websocket is None:
            self._bo_websocket = BO_WebSocket()
        return self._bo_websocket

    @property
    def group_test(self):
        if self._group_test is None:
            self._group_test = self.bo_websocket.get_group_test_by_id(self.group_test_id)
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
            questions = self.bo_websocket.get_all_questions_in_test(self.group_test.test_id)
            self._questions = defaultdict(list)
            for q in questions:
                self._questions[q.difficulty].append(q)
        return self._questions

    @property
    def test(self):
        if self._test is None:
            self._test = self.bo_websocket.get_test_by_id(self.group_test.test_id)
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

    def is_active(self):
        return self.is_exist() and self.group_test.is_active()

    def is_exist(self):
        return self.group_test is not None