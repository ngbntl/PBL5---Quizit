import pymssql

from Backend.DataAccess import get_MS_database, generate_id
from Backend.Model.DB_model import Group


class DAO_group:
    # SELECT
    def get_groups_by_teacher(self, teacher_id: str, is_show: bool = True) -> list[Group]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [group] WHERE [teacher_id] = %s AND [is_show] = %s", (teacher_id, is_show))
            return [Group(row) for row in cursor.fetchall()]

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
        if data.name is None:
            raise Exception("name is required!")
        failed_count = 0
        with get_MS_database(False) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [group]([id], [teacher_id], [name], [image_path])  VALUES (%s, %s, %s, %s)", (id, data.teacher_id, data.name, data.image_path))
                    return id
                except pymssql.Error as e:
                    if failed_count == 0 and id not in str(e.args[1]):
                        raise e
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    # UPDATE
    def update_group(self, data: Group):
        with get_MS_database(False) as cursor:
            sql = "UPDATE [group] SET "
            placeholder = []
            values = tuple()
            if data.name is not None:
                placeholder.append("[name] = %s")
                values += (data.name,)
            if data.is_show is not None:
                placeholder.append("[is_show] = %s")
                values += (data.is_show,)
            if data.image_path is not None:
                placeholder.append("[image_path] = %s")
                values += (data.image_path,)
            if len(values) == 0:
                raise Exception("No data to update!")
            sql += ",".join(placeholder) + " WHERE [id] = %s AND [teacher_id] = %s"
            values += (data.id, data.teacher_id)
            cursor.execute(sql, values)
