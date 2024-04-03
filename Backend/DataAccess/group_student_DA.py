from . import get_database
from ..Model.db_model import Student

class group_student_DA:
    # SELECT
    def get_all_students(self, group_id: str) -> list[Student]:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [group_student] WHERE [group_id] = %s", group_id)
            return cursor.fetchall()

    # INSERT
    def insert_student(self, group_id: str, student_id: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [group_student]([group_id], [student_id])  VALUES (%s, %s)", (group_id, student_id))