import pymssql

from Backend.DataAccess import get_MS_database, generate_id
from Backend.Model.DB_model import Group


class DAO_group:
    # SELECT
    def get_groups_by_teacher(self, teacher_id: str, is_show: bool = True) -> list[Group]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [group] WHERE [teacher_id] = %s AND [is_show] = %s", (teacher_id, is_show))
            return [Group(record) for record in cursor.fetchall()]

    def get_group_by_id(self, group_id: str) -> Group:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [group] WHERE [id] = %s", group_id)
            row = cursor.fetchone()
            return Group(row) if row else None

    def check_owner(self, group_id: str, teacher_id: str) -> bool:
        with get_MS_database(False) as cursor:
            cursor.execute("SELECT TOP 1 [id] FROM [group] WHERE [id] = %s AND [teacher_id] = %s", (group_id, teacher_id))
            return cursor.fetchone() is not None

    # INSERT
    def insert_group(self, data: Group) -> str:
        failed_count = 0
        with get_MS_database(False) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [group]([id], [teacher_id], [name])  VALUES (%s, %s, %s)",
                                   (id, data.teacher_id, data.name))
                    return id
                except pymssql.Error as e:
                    if failed_count == 0 and id not in str(e.args[1]):
                        raise e
                    failed_count += 1
                    if failed_count > 5:
                        raise e

    # UPDATE
    def update_visibility(self, group_id: str, is_show: bool):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [group] SET [is_show] = %s WHERE [id] = %s", (is_show, group_id))

    def update_group_name(self, group_id: str, name: str):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [group] SET [name] = %s WHERE [id] = %s", (name, group_id))
