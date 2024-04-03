from ..Model.db_model import Admin
from ..DataAccess import get_database


class admin_DA:
    # QUERY
    def get_admin_by_credential(self, username, hash_pswd) -> Admin | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM admin WHERE username=%s AND hash_pswd=%s", (username, hash_pswd))
            row = cursor.fetchone()
            return Admin(row) if row else None

    # INSERT
    def insert_admin(self, username, hash_pswd, name) -> None:
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO admin (username, hash_pswd, name) VALUES (%s, %s, %s)",
                           (username, hash_pswd, name))

    # update
    def ban_admin(self, admin_id) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE admin SET is_banned=1 WHERE id=%s", admin_id)

    def unban_admin(self, admin_id) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE admin SET is_banned=0 WHERE id=%s", admin_id)