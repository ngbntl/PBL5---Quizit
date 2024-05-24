import pickle

from Backend.DataAccess import get_MS_database
from Backend.Model.DB_model import StudentTest


class DAO_student_test:
    # INSERT
    def insert_student_test(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute(
                "INSERT INTO [student_test]([student_id], [group_test_id], [student_work])  VALUES (%s, %s, %s)",
                (data.student_id, data.group_test_id, pickle.dumps(data.student_work)))

    # SELECT:
    def get_student_test_by_group_test_id(self, student_id: str, group_test_id: str) -> StudentTest:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student_test] WHERE [student_id]=%s AND [group_test_id]=%s",
                           (student_id, group_test_id))
            row = cursor.fetchone()
            return StudentTest(row) if row else None

    def get_student_tests(self, group_test_id: str) -> list[StudentTest]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student_test] WHERE [group_test_id]=%s", (group_test_id,))
            return [StudentTest(row) for row in cursor.fetchall()]

    def get_student_test(self, group_test_id: str, student_id: str) -> StudentTest:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student_test] WHERE [group_test_id]=%s AND [student_id]=%s",
                           (group_test_id, student_id))
            row = cursor.fetchone()
            return StudentTest(row) if row else None

    def get_student_points(self, group_test_id: str) -> list[StudentTest]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT [student_id], [score] FROM [student_test] WHERE [group_test_id]=%s", (group_test_id,))
            return [StudentTest(row) for row in cursor.fetchall()]

    # UPDATE
    def submit(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute(
                "UPDATE [student_test] SET [student_work]=%s, [end]=%s, [score]=%s WHERE [student_id]=%s AND [group_test_id]=%s",
                (pickle.dumps(data.student_work), data.end, data.score, data.student_id, data.group_test_id))

    def update_student_work(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [student_test] SET [student_work]=%s WHERE [student_id]=%s AND [group_test_id]=%s",
                           (pickle.dumps(data.student_work), data.student_id, data.group_test_id))
