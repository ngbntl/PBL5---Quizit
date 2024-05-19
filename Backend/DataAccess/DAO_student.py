import pymssql

from Backend.DataAccess import get_MS_database, generate_id
from Backend.Model.DB_model import Student


class DAO_student:
    # SELECT
    def get_student_by_email(self, email: str) -> Student | None:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student] WHERE [email]=%s", (email,))
            row = cursor.fetchone()
            return Student(row) if row else None

    def get_student_by_id(self, student_id: str) -> Student | None:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [student] WHERE [id]=%s", (student_id,))
            row = cursor.fetchone()
            return Student(row) if row else None

    def get_student_list_id_by_list_email(self, list_email: list[str]) -> list[str]:
        list_email = list(set(list_email))
        with get_MS_database(False) as cursor:
            if len(list_email) == 1:
                cursor.execute(f"SELECT [id] FROM [student] WHERE [email] = %s", list_email[0])
            else:
                cursor.execute(f"SELECT [id] FROM [student] WHERE [email] IN {tuple(list_email)}")
            return [record[0] for record in cursor.fetchall()]

    # INSERT
    def insert_student(self, student: Student) -> str:
        if student.name is None:
            raise ValueError("Name is required!")

        failed_count = 0
        with get_MS_database(False) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [student]([id], [email], [hash_pswd], [name])  VALUES (%s, %s, %s, %s)",
                                   (id, student.email, student.hash_pswd, student.name))
                    return id
                except pymssql.Error as e:
                    if failed_count == 0 and id not in str(e.args[1]):
                        raise e
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    # UPDATE
    def update_is_banned(self, student_id: str, is_banned: bool):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [student] SET [is_banned]=%s WHERE [id]=%s", (is_banned, student_id))

    def update_is_verified(self, student_id: str, is_verified: bool):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [student] SET [is_verified]=%s WHERE [id]=%s", (is_verified, student_id))

    def update_avatar_path(self, student_id: str, avatar_path: str):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [student] SET [avatar_path]=%s WHERE [id]=%s", (avatar_path, student_id))

    def update_student(self, student):
        with get_MS_database(False) as cursor:
            sql = "UPDATE [student] SET "
            placeholder = []
            params = tuple()
            if student.hash_pswd is not None:
                placeholder.append("[hash_pswd] = %s")
                params += (student.hash_pswd,)
            if student.name is not None:
                placeholder.append("[name] = %s")
                params += (student.name,)
            if len(params) == 0:
                return
            sql += ",".join(placeholder) + " WHERE [id] = %s"
            params += (student.id,)
            cursor.execute(sql, params)
