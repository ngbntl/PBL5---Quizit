import pymssql

from Backend.DataAccess import get_MS_database, generate_id
from Backend.Model.DB_model import Admin


class DAO_admin:
    # QUERY
    def get_admin_by_credential(self, username, hash_pswd) -> Admin | None:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [admin] WHERE [username]=%s AND [hash_pswd]=%s", (username, hash_pswd))
            row = cursor.fetchone()
            return Admin(row) if row else None

    # INSERT
    def insert_admin(self, username, hash_pswd, name) -> str:
        failed_count = 0
        with get_MS_database(False) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [admin]([id], [username], [hash_pswd], [name])  VALUES (%s, %s, %s, %s)",
                                   (id, username, hash_pswd, name))
                    return id
                except pymssql.Error as e:
                    if failed_count == 0 and id not in str(e.args[1]):
                        raise e
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    # UPDATE
    def ban_admin(self, admin_id) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [admin] SET [is_banned]=1 WHERE [id]=%s", admin_id)

    def unban_admin(self, admin_id) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [admin] SET [is_banned]=0 WHERE [id]=%s", admin_id)
