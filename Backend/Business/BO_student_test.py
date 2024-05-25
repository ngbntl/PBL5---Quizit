from datetime import datetime

from Backend.Business.BO_group_test import BO_group_test
from Backend.DataAccess.DAO_group_test import DAO_group_test
from Backend.Model.DB_model import StudentTest, StudentWork_Question
from Backend.DataAccess.DAO_student_test import DAO_student_test
from Backend.Model.request_model import Req_StudentWork
from Backend.Model.response_model import Res_StudentTest


class BO_student_test:
    def __init__(self):
        self._dao_student_test = None
        self._dao_group_test = None
        self._bo_group_test = None

    @property
    def dao_student_test(self):
        if not self._dao_student_test:
            self._dao_student_test = DAO_student_test()
        return self._dao_student_test

    @property
    def dao_group_test(self):
        if not self._dao_group_test:
            self._dao_group_test = DAO_group_test()
        return self._dao_group_test

    @property
    def bo_group_test(self):
        if not self._bo_group_test:
            self._bo_group_test = BO_group_test()
        return self._bo_group_test

    def get_student_test_by_group_test_id(self, student_id: str, group_test_id: str) -> StudentTest:
        group_test = self.dao_group_test.get_group_test_by_id(group_test_id)
        if group_test is None:
            raise Exception("Group test does not exist")
        if datetime.now() < group_test.start:
            raise Exception("Group test has not started yet")
        if datetime.now() > group_test.end:
            raise Exception("Group test has ended")
        student_test = self.dao_student_test.get_student_test_by_group_test_id(student_id, group_test_id)
        if student_test is not None:
            if student_test.end is None:  # Student test exists but not submitted
                return student_test
            else:
                raise Exception("Student has already been submitted the test")
        # Student test does not exist. Now create.
        return self.insert_student_test(student_id, group_test_id)

    def get_group_test_in_time(self, student_id: str, start: datetime, end: datetime):
        return self.dao_group_test.get_group_test_for_student(student_id, start, end)

    # INSERT
    def insert_student_test(self, student_id: str, group_test_id: str) -> StudentTest:
        student_work = self.bo_group_test.generate_student_work(group_test_id)
        student_test = StudentTest(student_id=student_id, group_test_id=group_test_id, student_work=student_work)
        self.dao_student_test.insert_student_test(student_test)
        return Res_StudentTest.from_DB_model(student_test)

    def get_student_work(self, student_id: str, group_test_id: str):
        return self.dao_student_test.get_student_work(student_id, group_test_id)

    # UPDATE
    def submit(self, student_id: str, data: Req_StudentWork) -> float:
        student_test = self.dao_student_test.get_student_test_by_group_test_id(student_id, data.group_test_id)
        if student_test is None:
            raise Exception("Student test does not exist")
        if student_test.end is not None:
            raise Exception("Student test has already been submitted")
        for index, answer in enumerate(data.student_answer):
            student_test.student_work[index].student_answer = answer

        student_test.end = datetime.now()
        student_test.score = self.calculate_point(student_test.student_work)
        self.dao_student_test.submit(student_test)
        return student_test.score

    def calculate_point(self, student_work: list[StudentWork_Question]) -> float:
        score = .0
        for sw_question in student_work:
            if sw_question.student_answer is None:
                continue

            score += len(set(sw_question.student_answer) & sw_question.answer.correct) / len(sw_question.answer.correct)

        return score / len(student_work)


