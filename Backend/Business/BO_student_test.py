import pickle
from datetime import datetime

from Backend.Business.BO_group_test import BO_group_test
from Backend.DataAccess.DAO_group_test import DAO_group_test
from Backend.Model.DB_model import StudentTest
from Backend.DataAccess.DAO_student_test import DAO_student_test
from Backend.Model.request_model import Req_StudentTest, Req_StudentWork
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

    def get_student_test(self, data: Req_StudentTest) -> Res_StudentTest:
        group_test = self.dao_group_test.get_group_test_by_id(data.group_test_id)
        if group_test is None:
            raise Exception("Group test does not exist")
        if datetime.now() < group_test.start:
            raise Exception("Group test has not started yet")
        if datetime.now() > group_test.end:
            raise Exception("Group test has ended")
        student_test = self.dao_student_test.get_student_test(
            StudentTest(data.model_dump(exclude_none=True, exclude_unset=True)))
        if student_test is not None:
            return Res_StudentTest(student_id=student_test.student_id, group_test_id=student_test.group_test_id,
                                   start=student_test.start, end=student_test.end, score=student_test.score,
                                   student_work=pickle.loads(student_test.student_work))
        # Student test does not exist. Now create.
        return self.insert_student_test(data)

    # INSERT
    def insert_student_test(self, data: Req_StudentTest) -> Res_StudentTest:
        student_work = self.bo_group_test.generate_student_work(data.group_test_id)
        student_test = StudentTest({'student_id': data.student_id, 'group_test_id': data.group_test_id,
                                    'student_work': pickle.dumps(student_work)})
        self.dao_student_test.insert_student_test(student_test)
        return Res_StudentTest(student_id=data.student_id, group_test_id=data.group_test_id, student_work=student_work)

    def get_student_work(self, student_id: str, group_test_id: str):
        return self.dao_student_test.get_student_work(student_id, group_test_id)

    # UPDATE
    def submit(self, student_id: str, data: Req_StudentWork) -> float:
        student_test = self.dao_student_test.get_student_test(
            StudentTest({'student_id': student_id, 'group_test_id': data.group_test_id}))
        if student_test is None:
            raise Exception("Student test does not exist")
        if datetime.now() < student_test.start:
            raise Exception("Student test has not started yet")
        if datetime.now() > student_test.end:
            raise Exception("Student test has ended")

        std_tst = Res_StudentTest(student_id=student_test.student_id, group_test_id=student_test.group_test_id,
                                  start=student_test.start, end=student_test.end, score=student_test.score,
                                  student_work=pickle.loads(student_test.student_work))
        student_choices = data.student_choices
        for index in range(student_choices):
            std_tst.student_work[index].student_choices = student_choices[index]
