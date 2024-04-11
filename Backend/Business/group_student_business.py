from Backend.DataAccess.group_DA import group_DA
from Backend.DataAccess.group_student_DA import group_student_DA
from Backend.Business.group_business import group_business


class group_student_business:
    def __init__(self):
        self.group_student_DA = group_student_DA()

    # SELECT

    def get_group_id_by_student(self, student_id: str, is_join: bool = True) -> list[str]:
        return self.group_student_DA.get_group_id_by_student(student_id, is_join)

    def get_groups_by_student(self, student_id: str, is_join: bool = True) -> list[dict]:
        return self.group_student_DA.get_groups_by_student(student_id, is_join)

    def get_students_by_group(self, group_id: str, is_join: bool = True) -> list[str]:
        return self.group_student_DA.get_students_by_group(group_id, is_join)

    # INSERT
    def insert_student(self, group_id: str, student_id: str, teacher_id: str = None) -> None:
        if teacher_id and group_DA().check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        self.group_student_DA.insert_student(group_id=group_id, student_id=student_id)

    # UPDATE
    def accept_join_request(self, teacher_id: str, group_id: str, student_id: str):
        if group_DA().check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        self.group_student_DA.accept_join_request(group_id, student_id)

    def update_visibility(self, group_id: str, student_id: str, visibility: str):
        self.group_student_DA.update_visibility(group_id, student_id, visibility)

    # DELETE
    def delete_join_request(self, teacher_id: str, group_id: str, student_id: str):
        group = group_business().get_group_by_id(group_id)
        if group.get("teacher_id") != teacher_id:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        self.group_student_DA.delete_join_request(group_id, student_id)
