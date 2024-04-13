from Backend.DataAccess.group_DA import group_DA
from Backend.DataAccess.group_student_DA import group_student_DA
from Backend.Model.request_model import Req_GroupStudent


class group_student_BO:
    def __init__(self):
        self.group_student_DA = group_student_DA()

    # SELECT

    def get_group_id_by_student(self, student_id: str, is_join: bool = True) -> list[str]:
        return self.group_student_DA.get_group_id_by_student(student_id=student_id, is_join=is_join)

    def get_groups_by_student(self, student_id: str, is_join: bool = True) -> list[dict]:
        return self.group_student_DA.get_groups_by_student(student_id=student_id, is_join=is_join)

    def get_students_by_group(self, group_id: str, is_join: bool = True) -> list[dict]:
        return self.group_student_DA.get_students_by_group(group_id=group_id, is_join=is_join)

    # INSERT
    def insert_student(self, group_id: str, student_id: str, teacher_id: str = None) -> None:
        if group_id is None:
            raise ValueError("group_id is required!")
        if student_id is None:
            raise ValueError("student_id is required!")
        if teacher_id and group_DA().check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        self.group_student_DA.insert_student(group_id=group_id, student_id=student_id)

    def insert_students(self, teacher_id: str, group_id: str, list_id: str):
        if group_DA().check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        self.group_student_DA.insert_students(group_id=group_id, list_id=list_id)

    # UPDATE
    def update_join_request(self, teacher_id: str, group_id: str, student_id: str, accept: bool):
        if group_DA().check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        self.group_student_DA.update_join_request(group_id=group_id, student_id=student_id, accept=accept)

    def update_student_group(self, student_id: str, data: Req_GroupStudent):
        if data.is_show is not None:
            self.group_student_DA.update_visibility(group_id=data.group_id, student_id=student_id,
                                                    visibility=data.is_show)

    # DELETE
    # def delete_student(self, teacher_id: str, group_id: str, student_id: str):
    #     if group_DA().check_owner(group_id, teacher_id) is False:
    #         raise ValueError(f"group {group_id} does not belong to {teacher_id}")
    #     self.group_student_DA.delete_student(group_id=group_id, student_id=student_id)

    def delete_students(self, teacher_id: str, group_id: str, list_id: list[str]) -> None:
        if group_DA().check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        if len(list_id) != 0:
            self.group_student_DA.delete_students(group_id=group_id, list_id=list_id)

    def leave_group(self, student_id: str, group_id: str):
        self.group_student_DA.delete_student(student_id=student_id, group_id=group_id)
