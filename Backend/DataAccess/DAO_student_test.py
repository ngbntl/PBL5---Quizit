import pickle

from Backend.DataAccess import get_MS_database
from Backend.Model.DB_model import StudentTest, Student, GroupTest


class DAO_student_test:
    # INSERT
    def insert_student_test(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute(
                "INSERT INTO [student_test]([student_id], [group_test_id], [student_work])  VALUES (%s, %s, %s)",
                (data.student_id, data.group_test_id, pickle.dumps(data.student_work)))

    # SELECT:
    def get_student_tests(self, group_test_id: str) -> list[StudentTest]:
        with get_MS_database(True) as cursor:
            SQL = """
                SELECT s.[id], s.[name], s.[avatar_path], 
                       st.[start], st.[end], st.[student_work], st.[score], st.[violate] 
                FROM [student] s
                LEFT JOIN [student_test] st ON s.[id] = st.[student_id]
                WHERE s.[id] IN (SELECT [student_id] FROM [group_student] WHERE [group_id] = (SELECT [group_id] FROM [group_test] WHERE [id]=%s))
            """
            cursor.execute(SQL, (group_test_id,))
            return [StudentTest(row).set_student(Student(row)) for row in cursor.fetchall()]

    def get_student_test(self, group_test_id: str, student_id: str) -> StudentTest:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student_test] WHERE [group_test_id]=%s AND [student_id]=%s", (group_test_id, student_id))
            row = cursor.fetchone()
            return StudentTest(row) if row else None

    def get_students_score(self, group_test_id: str) -> list[tuple[Student, float]]:
        with get_MS_database(True) as cursor:
            sql = """
                SELECT s.[id], s.[name], s.[avatar_path], st.[score] 
                FROM [student_test] st JOIN [student] s ON st.[student_id] = s.[id]
                WHERE [group_test_id]=%s
            """
            cursor.execute(sql, (group_test_id,))
            return [(Student(row), row['score']) for row in cursor.fetchall()]

    def get_student_test_history(self, student_id: str, group_id: str) -> list[StudentTest]:
        sql = """
            SELECT st.[start], st.[end], st.[score], st.[violate],
                   gt.[id], gt.[test_id], gt.[name]
            FROM student_test st
            JOIN group_test gt ON st.group_test_id = gt.id
            WHERE st.student_id = %s AND gt.group_id = %s
        """
        with get_MS_database(True) as cursor:
            cursor.execute(sql, (student_id, group_id))
            arr = []
            for row in cursor.fetchall():
                st = StudentTest(start=row['start'], end=row['end'], score=row['score'], violate=row['violate'])
                st.group_test = GroupTest(id=row['id'], test_id=row['test_id'], name=row['name'])
                arr.append(st)
            return arr

    # UPDATE
    def submit(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute(
                "UPDATE [student_test] SET [student_work]=%s, [end]=%s, [score]=%s, [violate]=%s WHERE [student_id]=%s AND [group_test_id]=%s",
                (pickle.dumps(data.student_work), data.end, data.score, data.violate, data.student_id, data.group_test_id))

    def update_student_work(self, data: StudentTest):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [student_test] SET [student_work]=%s WHERE [student_id]=%s AND [group_test_id]=%s",
                           (pickle.dumps(data.student_work), data.student_id, data.group_test_id))

    def update_violate(self, group_test_id: str, student_id: str, violate: int):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [student_test] SET [violate]=%s WHERE [student_id]=%s AND [group_test_id]=%s",
                           (violate, student_id, group_test_id))