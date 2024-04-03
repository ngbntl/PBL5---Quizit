from . import get_database
from ..Model.db_model import Group


class group_DA:
    # SELECT
    def get_groups_by_teacher(self, teacher_id: str) -> list[Group]:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [group] WHERE [teacher_id] = %s", (teacher_id,))
            return [Group(row) for row in cursor.fetchall()]

    # INSERT
    def insert_group(self, teacher_id: str, name: str) -> str:
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [group]([teacher_id], [name])  VALUES (%s, %s)", (teacher_id, name))
            return cursor.lastrowid

    # UPDATE
    def update_is_show(self, group_id: str, is_show: bool):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [group] SET [is_show] = %s WHERE [id] = %s", (is_show, group_id))

    def update_group_name(self, group_id: str, name: str):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [group] SET [name] = %s WHERE [id] = %s", (name, group_id))
