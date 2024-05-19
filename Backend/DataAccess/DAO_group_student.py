from Backend.DataAccess import get_MS_database
from Backend.DataAccess.DAO_student import DAO_student
from Backend.Model.DB_model import Group, Student, GroupStudent


class DAO_group_student:
    def __init__(self):
        self._dao_student = None

    @property
    def dao_student(self):
        if self._dao_student is None:
            self._dao_student = DAO_student()
        return self._dao_student

    # SELECT
    def get_students_by_group(self, group_id: str, is_join: bool = True) -> list[Student]:
        with get_MS_database(True) as cursor:
            cursor.execute("""
                SELECT * FROM [student] WHERE [id] IN 
                (SELECT [student_id] from [group_student] WHERE [group_id] = %s AND [is_join] = %s)
            """, (group_id, is_join))
            return [Student(row) for row in cursor.fetchall()]

    def get_group_id_by_student(self, student_id: str, is_join: bool = True) -> list[str]:
        with get_MS_database(False) as cursor:
            cursor.execute("SELECT [group_id] FROM [group_student] WHERE [student_id] = %s AND [is_join] = %s",
                           (student_id, is_join))
            return [record[0] for record in cursor.fetchall()]

    def get_groups_by_student(self, student_id, is_join) -> list[Group]:
        with get_MS_database(True) as cursor:
            cursor.execute("""
                SELECT * FROM [group] WHERE [id] IN 
                (SELECT [group_id] FROM [group_student] WHERE [student_id] = %s AND [is_join] = %s)
            """, (student_id, is_join))
            return [Group(row) for row in cursor.fetchall()]

    def check_student_in_group(self, group_id: str, student_id: str, is_join=True) -> bool:
        with get_MS_database(False) as cursor:
            cursor.execute("SELECT TOP 1 [group_id] FROM [group_student] WHERE [group_id] = %s AND [student_id] = %s AND [is_join] = %s",
                           (group_id, student_id, is_join))
            return cursor.fetchone() is not None

    # INSERT
    def request_join(self, group_id: str, student_id: str) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("INSERT INTO [group_student]([group_id], [student_id], [is_join]) VALUES (%s, %s, 0)",
                           (group_id, student_id))

    def insert_students_by_id(self, group_id: str, list_id: list[str]) -> None:
        with get_MS_database(False) as cursor:
            for student_id in set(list_id):
                try:
                    cursor.execute(
                        "INSERT INTO [group_student]([group_id], [student_id], [is_join]) VALUES (%s, %s, 1)",
                        (group_id, student_id))
                except:
                    cursor.execute(
                        "UPDATE [group_student] SET [is_join] = 1 WHERE [group_id] = %s AND [student_id] = %s",
                        (group_id, student_id))

    # UPDATE
    def update(self, group_student: GroupStudent) -> None:
        sql = "UPDATE [group_student] SET "
        placeholder = list()
        values = tuple()
        with get_MS_database(False) as cursor:
            if group_student.is_show is not None:
                placeholder.append("[is_show] = %s")
                values += (group_student.is_show,)
            if group_student.is_join is not None:
                placeholder.append("[is_join] = %s")
                values += (group_student.is_join,)
            if len(values) == 0:
                return
            sql += ",".join(placeholder) + " WHERE [group_id] = %s AND [student_id] = %s"
            values += (group_student.group_id, group_student.student_id)
            cursor.execute(sql, values)

    # DELETE

    def delete_student(self, group_id: str, student_id: str):
        with get_MS_database(False) as cursor:
            cursor.execute("DELETE FROM [group_student] WHERE [group_id] = %s AND [student_id] = %s",
                           (group_id, student_id))

    def delete_students_by_id(self, group_id: str, list_id: list[str]):
        list_id = tuple(set(list_id))  # remove duplicate
        with get_MS_database(False) as cursor:
            cursor.execute("DELETE FROM [group_student] WHERE [group_id] = %s AND [student_id] IN %s",
                           (group_id, list_id))
