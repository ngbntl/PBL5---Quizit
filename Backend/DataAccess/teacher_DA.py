import pymssql

from Backend.DataAccess import get_database, generate_id


class teacher_DA:
    # SELECT
    def get_teacher_by_email(self, email: str) -> dict | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [teacher] WHERE [email]=%s", (email,))
            row = cursor.fetchone()
            if row is not None:
                return row
            return None

    def get_teacher_by_id(self, teacher_id: str) -> dict | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [teacher] WHERE [id]=%s", (teacher_id,))
            row = cursor.fetchone()
            if row is not None:
                return row
            return None

    # INSERT
    def insert_teacher(self, email: str, hash_pswd: str, name: str):
        failed_count = 0
        with get_database(True) as cursor:
            duplicate_id = False
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [teacher]([id], [email], [hash_pswd], [name])  VALUES (%s, %s, %s, %s)",
                                   (id, email, hash_pswd, name))
                    return id
                except pymssql.Error as e:
                    if duplicate_id is False and id not in str(e.args[1]):
                        raise e
                    duplicate_id = True

                    failed_count += 1
                    if failed_count == 5:
                        raise e

    # UPDATE
    def update_password(self, teacher_id: str, hash_pswd: str):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [teacher] SET [hash_pswd]=%s WHERE [id]=%s", (hash_pswd, teacher_id))

    def update_name(self, teacher_id: str, name: str):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [teacher] SET [name]=%s WHERE [id]=%s", (name, teacher_id))

    def update_is_banned(self, teacher_id: str, is_banned: bool):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [teacher] SET [is_banned]=%s WHERE [id]=%s", (is_banned, teacher_id))

    def update_is_verified(self, teacher_id: str, is_verified: bool):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [teacher] SET [is_verified]=%s WHERE [id]=%s", (is_verified, teacher_id))

    def update_avatar_path(self, teacher_id: str, avatar_path: str):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [teacher] SET [avatar_path]=%s WHERE [id]=%s", (avatar_path, teacher_id))
