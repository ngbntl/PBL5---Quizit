from Backend.Business.BO_group_test import BO_group_test
from Backend.Model.DB_model import StudentTest
from Backend.DataAccess.DAO_group_test import DAO_group_test
from Backend.DataAccess.DAO_student_test import DAO_student_test


class BO_student_test:
    def __init__(self):
        self._dao_student_test = None
        self._bo_group_test = None

    @property
    def dao_student_test(self):
        if not self._dao_student_test:
            self._dao_student_test = DAO_student_test()
        return self._dao_student_test

    @property
    def bo_group_test(self):
        if not self._bo_group_test:
            self._bo_group_test = BO_group_test()
        return self._bo_group_test

    def get_student_test(self, data: StudentTest):
        student_test = self.dao_student_test.get_student_test(data)
        if student_test is not None:
            return student_test
        # Student test does not exist. Now create.
        return self.insert_student_test(data)

    # INSERT
    def insert_student_test(self, data: StudentTest) -> StudentTest:
        data.student_work = self.bo_group_test.generate_test_for_student(data.group_test_id)
        return self.dao_student_test.insert_student_test(data)

    def get_student_work(self, student_id: str, group_test_id: str):
        return self.dao_student_test.get_student_work(student_id, group_test_id)
