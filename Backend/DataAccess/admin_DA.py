from Backend.DataAccess import get_database, generate_id


class admin_DA:
    # QUERY
    def get_admin_by_credential(self, username, hash_pswd) -> dict | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [admin] WHERE [username]=%s AND [hash_pswd]=%s", (username, hash_pswd))
            row = cursor.fetchone()
            return row if row else None

    # INSERT
    def insert_admin(self, username, hash_pswd, name) -> str:
        failed_count = 0
        with get_database(True) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [admin]([id], [username], [hash_pswd], [name])  VALUES (%s, %s, %s, %s)",
                                   (id, username, hash_pswd, name))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count > 5:
                        raise e

    # UPDATE
    def ban_admin(self, admin_id) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [admin] SET [is_banned]=1 WHERE [id]=%s", admin_id)

    def unban_admin(self, admin_id) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [admin] SET [is_banned]=0 WHERE [id]=%s", admin_id)
