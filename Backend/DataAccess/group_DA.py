from Backend.DataAccess import get_database, generate_id
from Backend.Model.db_model import Group


class group_DA:
    # SELECT
    def get_groups_by_teacher(self, teacher_id: str, is_show: bool = True) -> list[dict]:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [group] WHERE [teacher_id] = %s AND [is_show] = %s", (teacher_id, is_show))
            return cursor.fetchall()

    def get_group_by_id(self, group_id: str) -> dict:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [group] WHERE [id] = %s", group_id)
            return cursor.fetchone()

    def check_owner(self, group_id: str, teacher_id: str) -> bool:
        with get_database(False) as cursor:
            cursor.execute("SELECT [id] FROM [group] WHERE [id] = %s AND [teacher_id] = %s", (group_id, teacher_id))
            return cursor.fetchone() is not None

    # INSERT
    def insert_group(self, teacher_id: str, name: str) -> str:
        failed_count = 0
        with get_database(True) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [group]([id], [teacher_id], [name])  VALUES (%s, %s, %s)",
                                   (id, teacher_id, name))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count > 5:
                        raise e

    # UPDATE
    def update_visibility(self, group_id: str, is_show: bool):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [group] SET [is_show] = %s WHERE [id] = %s", (is_show, group_id))

    def update_group_name(self, group_id: str, name: str):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [group] SET [name] = %s WHERE [id] = %s", (name, group_id))
