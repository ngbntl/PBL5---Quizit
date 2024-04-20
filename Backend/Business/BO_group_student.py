from Backend.DataAccess.DAO_group import DAO_group
from Backend.DataAccess.DAO_group_student import DAO_group_student
from Backend.Model.DB_model import Group, Student
from Backend.Model.request_model import Req_GroupStudent


class BO_group_student:
    def __init__(self):
        self._dao_group_student = None
        self._dao_group = None

    @property
    def dao_group_student(self):
        if self._dao_group_student is None:
            self._dao_group_student = DAO_group_student()
        return self._dao_group_student

    @property
    def dao_group(self):
        if self._dao_group is None:
            self._dao_group = DAO_group()
        return self._dao_group

    # SELECT
    def get_group_id_by_student(self, student_id: str, is_join: bool = True) -> list[str]:
        return self.dao_group_student.get_group_id_by_student(student_id=student_id, is_join=is_join)

    def get_groups_by_student(self, student_id: str, is_join: bool = True) -> list[Group]:
        return self.dao_group_student.get_groups_by_student(student_id=student_id, is_join=is_join)

    def get_students_by_group(self, group_id: str, is_join: bool = True) -> list[Student]:
        return self.dao_group_student.get_students_by_group(group_id=group_id, is_join=is_join)

    # INSERT
    def request_join(self, group_id: str, student_id: str) -> None:
        if group_id is None:
            raise ValueError("group_id is required!")
        if student_id is None:
            raise ValueError("student_id is required!")
        self.dao_group_student.request_join(group_id=group_id, student_id=student_id)

    def insert_students(self, teacher_id: str, group_id: str, list_id: str):
        if DAO_group().check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        self.dao_group_student.insert_students(group_id=group_id, list_id=list_id)

    # UPDATE
    # def update_join_requests(self, teacher_id: str, group_id: str, student_id: str, accept: bool):
    #     if DAO_group().check_owner(group_id, teacher_id) is False:
    #         raise ValueError(f"group {group_id} does not belong to {teacher_id}")
    #     self.dao_group_student.update_join_requests(group_id=group_id, student_id=student_id, accept=accept)

    def update_student_group(self, student_id: str, data: Req_GroupStudent):
        if data.is_show is not None:
            self.dao_group_student.update_visibility(group_id=data.group_id, student_id=student_id,
                                                     visibility=data.is_show)

    # DELETE
    # def delete_student(self, teacher_id: str, group_id: str, student_id: str):
    #     if group_DA().check_owner(group_id, teacher_id) is False:
    #         raise ValueError(f"group {group_id} does not belong to {teacher_id}")
    #     self.group_student_DA.delete_student(group_id=group_id, student_id=student_id)

    def delete_students(self, teacher_id: str, group_id: str, list_id: list[str]) -> None:
        if DAO_group().check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")
        if len(list_id) != 0:
            self.dao_group_student.delete_students(group_id=group_id, list_id=list_id)

    def leave_group(self, student_id: str, group_id: str):
        self.dao_group_student.delete_student(student_id=student_id, group_id=group_id)
