from Backend.DataAccess.group_DA import group_DA
from Backend.Model.request_model import Req_Group


class group_business:
    def __init__(self):
        self.group_DA = group_DA()

    # SELECT
    def get_groups_by_teacher(self, teacher_id: str, is_show: bool = True) -> list[dict]:
        return self.group_DA.get_groups_by_teacher(teacher_id, is_show)

    def get_group_by_id(self, group_id: str, teacher_id: str | None = None) -> dict | None:
        group = self.group_DA.get_group_by_id(group_id)
        if teacher_id and group.get('teacher_id') != teacher_id:
            raise Exception(f"Group {group_id} is not belong to teacher {teacher_id}!")
        return group

    # INSERT
    def insert_group(self, teacher_id: str, data: Req_Group) -> str:
        if data.name is None:
            raise Exception("name is required!")
        return self.group_DA.insert_group(teacher_id, data.name)

    # UPDATE
    def update_visibility(self, teacher_id: str, group_id: str, visibility: bool):
        if self.group_DA.check_owner(group_id, teacher_id) is False:
            raise Exception(f"Group {group_id} is not belong to teacher {teacher_id}!")
        self.group_DA.update_visibility(group_id, visibility)

    def update_group_name(self, group_id: str, name: str):
        self.group_DA.update_group_name(group_id, name)
