from Backend.DataAccess.DAO_group import DAO_group
from Backend.DataAccess.DAO_group_test import DAO_group_test
from Backend.Model.DB_model import GroupTest
from Backend.Model.request_model import Req_GroupTest
from Backend.Model.response_model import Res_GroupTest


class BO_group_test:
    def __init__(self):
        self._dao_group_test = None
        self._dao_group = None

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

    # INSERT
    def insert_group_test(self, teacher_id: str, data: Req_GroupTest) -> str:
        if self.dao_group.check_owner(data.group_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of group {data.group_id}")
        group_test = GroupTest(data.model_dump(exclude_none=True, exclude_unset=True, exclude={'id'}))
        return self.dao_group_test.insert_group_test(group_test)

    # SELECT
    def get_group_test(self, group_id: str) -> list[Res_GroupTest]:
        return [Res_GroupTest(**group_test.__dict__) for group_test in self.dao_group_test.get_group_test(group_id)]
