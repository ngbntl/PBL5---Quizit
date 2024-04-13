from Backend.DataAccess.group_DA import group_DA
from Backend.Model.request_model import Req_Group


class group_BO:
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
    def update_group(self, teacher_id: str, data: Req_Group):
        if self.group_DA.check_owner(data.id, teacher_id) is False:
            raise Exception(f"Group {data.id} is not belong to teacher {teacher_id}!")
        if data.is_show is not None:
            self.group_DA.update_visibility(group_id=data.id, is_show=data.is_show)
        if data.name is not None:
            self.group_DA.update_group_name(group_id=data.id, name=data.name)
