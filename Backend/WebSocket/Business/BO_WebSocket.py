from Backend.Business.BO_group import BO_group
from Backend.Business.BO_group_student import BO_group_student
from Backend.Business.BO_group_test import BO_group_test
from Backend.Business.BO_test import BO_test
from Backend.Model.DB_model import GroupTest, Question


class BO_WebSocket:
    def __init__(self):
        self._bo_group_test = None
        self._bo_group = None
        self._bo_group_student = None
        self._bo_test = None

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

    @property
    def bo_test(self):
        if self._bo_test is None:
            self._bo_test = BO_test()
        return self._bo_test

    def get_test_by_id(self, test_id: str):
        return self.bo_test.get_test_by_id(test_id)

    def get_group_test_by_id(self, group_test_id: str) -> GroupTest:
        return self.bo_group_test.get_group_test_by_id(group_test_id)

    def check_student_in_group(self, group_id: str, student_id: str) -> bool:
        return self.bo_group_student.check_student_in_group(group_id, student_id)

    def get_group_test_by_group(self, group_id: str) -> list[GroupTest]:
        return self.bo_group_test.get_group_test_by_group(group_id)

    def get_all_questions_in_test(self, test_id: str) -> list[Question]:
        return self.bo_group_test.get_all_questions_in_test(test_id)
