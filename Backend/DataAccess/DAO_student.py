import pymssql

from Backend.DataAccess import get_MS_database, DAO_test
from Backend.Model.DB_model import Student
from Backend.Model.request_model import Req_Student


class DAO_student:
    # SELECT
    def get_student_by_email(self, email: str) -> Student | None:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student] WHERE [email]=%s", (email,))
            row = cursor.fetchone()
            if row is not None:
                return Student(row)
            return None

    def get_student_by_id(self, student_id: str) -> Student | None:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student] WHERE [id]=%s", (student_id,))
            row = cursor.fetchone()
            if row is not None:
                return Student(row)
            return None

    # INSERT
    def insert_student(self, email: str, name: str, hash_pswd: str) -> str:
        failed_count = 0
        with get_MS_database(True) as cursor:
            duplicate_id = False
            while True:
                id = DAO_test(8)
                try:
                    cursor.execute("INSERT INTO [student]([id], [email], [hash_pswd], [name])  VALUES (%s, %s, %s, %s)",
                                   (id, email, hash_pswd, name))
                    return id
                except pymssql.Error as e:
                    if duplicate_id is False and id not in str(e.args[1]):
                        raise e
                    duplicate_id = True

                    failed_count += 1
                    if failed_count > 5:
                        raise e

    # UPDATE
    def update_password(self, student_id: str, hash_pswd: str):
        with get_MS_database(True) as cursor:
            cursor.execute("UPDATE [student] SET [hash_pswd]=%s WHERE [id]=%s", (hash_pswd, student_id))

    def update_name(self, student_id: str, name: str):
        with get_MS_database(True) as cursor:
            cursor.execute("UPDATE [student] SET [name]=%s WHERE [id]=%s", (name, student_id))

    def update_is_banned(self, student_id: str, is_banned: bool):
        with get_MS_database(True) as cursor:
            cursor.execute("UPDATE [student] SET [is_banned]=%s WHERE [id]=%s", (is_banned, student_id))

    def update_is_verified(self, student_id: str, is_verified: bool):
        with get_MS_database(True) as cursor:
            cursor.execute("UPDATE [student] SET [is_verified]=%s WHERE [id]=%s", (is_verified, student_id))

    def update_avatar_path(self, student_id: str, avatar_path: str):
        with get_MS_database(True) as cursor:
            cursor.execute("UPDATE [student] SET [avatar_path]=%s WHERE [id]=%s", (avatar_path, student_id))
