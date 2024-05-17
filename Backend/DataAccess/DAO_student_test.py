from datetime import datetime

from Backend.DataAccess import get_MS_database
from Backend.Model.DB_model import StudentTest


class DAO_student_test:
    # INSERT
    def insert_student_test(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute(
                "INSERT INTO [student_test]([student_id], [group_test_id], [student_work])  VALUES (%s, %s, %s)",
                (data.student_id, data.group_test_id, data.student_work))

    # SELECT:
    def get_student_test(self, data: StudentTest) -> StudentTest:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student_test] WHERE [student_id]=%s AND [group_test_id]=%s",
                           (data.student_id, data.group_test_id))
            row = cursor.fetchone()
            return StudentTest(row) if row else None

    # UPDATE
    def submit(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute(
                "UPDATE [student_test] SET [student_work]=%s, [end]=%s, [score]=%s WHERE [student_id]=%s AND [group_test_id]=%s",
                (data.student_work, data.end, data.score, data.student_id, data.group_test_id))

    def update_student_work(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [student_test] SET [student_work]=%s WHERE [student_id]=%s AND [group_test_id]=%s",
                           (data.student_work, data.student_id, data.group_test_id))
