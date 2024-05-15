import pickle

from Backend.DataAccess.DAO_group import DAO_group
from Backend.DataAccess.DAO_group_test import DAO_group_test
from Backend.DataAccess.DAO_question import DAO_question
from Backend.DataAccess.DAO_test import DAO_test
from Backend.DataAccess.DAO_test_structure import DAO_test_structure
from Backend.Model.DB_model import GroupTest
from Backend.Model.request_model import Req_GroupTest, Req_NumberOfQuestion
from Backend.Model.response_model import Res_StudentTestQuestion


class BO_group_test:
    def __init__(self):
        self._dao_group_test = None
        self._dao_group = None
        self._dao_test = None
        self._dao_test_structure = None
        self._dao_question = None

    @property
    def dao_group_test(self):
        if not self._dao_group_test:
            self._dao_group_test = DAO_group_test()
        return self._dao_group_test

    @property
    def dao_group(self):
        if not self._dao_group:
            self._dao_group = DAO_group()
        return self._dao_group

    @property
    def dao_test(self):
        if not self._dao_test:
            self._dao_test = DAO_test()
        return self._dao_test

    @property
    def dao_test_structure(self):
        if not self._dao_test_structure:
            self._dao_test_structure = DAO_test_structure()
        return self._dao_test_structure

    @property
    def dao_question(self):
        if not self._dao_question:
            self._dao_question = DAO_question()
        return self._dao_question

    # INSERT
    def insert_group_test(self, teacher_id: str, data: Req_GroupTest) -> str:
        if self.dao_group.check_owner(data.group_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of group {data.group_id}")
        group_test = GroupTest(data.model_dump(exclude_none=True, exclude_unset=True, exclude={'id'}))
        return self.dao_group_test.insert_group_test(group_test)

    # SELECT
    def get_group_test_in_group(self, group_id: str) -> list[GroupTest]:
        return self.dao_group_test.get_group_test_by_group(group_id)

    def generate_student_work(self, group_test_id: str) -> list[Res_StudentTestQuestion]:
        # Get group test by id
        grp_ts = self.dao_group_test.get_group_test_by_id(group_test_id)
        if grp_ts is None:
            raise Exception(f"Group test {group_test_id} not found")
        # Then get test by id
        test = self.dao_test.get_test_by_id(grp_ts.test_id)
        # Get test structure
        test_struct = self.dao_test_structure.get_structure(test.id)
        # For each test structure, get the number of question then get the question
        for ts in test_struct:
            noq: list[Req_NumberOfQuestion] = pickle.loads(ts.number_of_question)
            for n in noq:
                pass

    # UPDATE
    def update_group_test(self, teacher_id: str, data: Req_GroupTest):
        group_test = self.dao_group_test.get_group_test_by_id(data.id)

        if self.dao_group.check_owner(group_test.group_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of group {group_test.group_id}")
        if self.dao_test.check_owner(group_test.test_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of test {group_test.test_id}")

        if not group_test:
            raise Exception(f"Group test {data.id} not found")

        if data.start is not None:
            group_test.start = data.start
        if data.end is not None:
            group_test.end = data.end
        if data.duration is not None:
            group_test.duration = data.duration
        if data.shuffle is not None:
            group_test.shuffle = data.shuffle

        self.dao_group_test.update_group_test(group_test)

    # DELETE
    def delete_group_test(self, teacher_id: str, group_test_id: str):
        group_test = self.dao_group_test.get_group_test_by_id(group_test_id)

        if not group_test:
            raise Exception(f"Group test {group_test_id} not found")
        if self.dao_group.check_owner(group_test.group_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of group {group_test.group_id}")

        self.dao_group_test.delete_group_test(group_test_id)
