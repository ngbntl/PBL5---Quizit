from Backend.DataAccess.DAO_group import DAO_group
from Backend.Model.DB_model import Group
from Backend.Model.request_model import Req_Group


class BO_group:
    def __init__(self):
        self._dao_group = None

    @property
    def dao_group(self) -> DAO_group:
        if self._dao_group is None:
            self._dao_group = DAO_group()
        return self._dao_group

    # SELECT
    def get_groups_by_teacher(self, teacher_id: str, is_show: bool = True) -> list[Group]:
        return self.dao_group.get_groups_by_teacher(teacher_id=teacher_id, is_show=is_show)

    def get_group_by_id(self, group_id: str, teacher_id: str | None = None) -> Group:
        group = self.dao_group.get_group_by_id(group_id)
        if teacher_id and group.teacher_id != teacher_id:
            raise Exception(f"Group {group_id} is not belong to teacher {teacher_id}!")
        return group

    # INSERT
    def insert_group(self, teacher_id: str, data: Req_Group) -> str:
        if data.name is None:
            raise Exception("name is required!")
        return self.dao_group.insert_group(teacher_id, data.name)

    # UPDATE
    def update_group(self, teacher_id: str, data: Req_Group):
        if self.dao_group.check_owner(data.id, teacher_id) is False:
            raise Exception(f"Group {data.id} is not belong to teacher {teacher_id}!")
        if data.is_show is not None:
            self.dao_group.update_visibility(group_id=data.id, is_show=data.is_show)
        if data.name is not None:
            self.dao_group.update_group_name(group_id=data.id, name=data.name)

    def delete_group(self, teacher_id: str, data: Req_Group):
        if self.dao_group.check_owner(data.id, teacher_id) is False:
            raise Exception(f"Group {data.id} is not belong to teacher {teacher_id}!")
        if data.name is not None:
            self.dao_collection.delete_group(id=data.id)
