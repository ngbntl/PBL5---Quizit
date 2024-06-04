from datetime import datetime

import pymssql

from Backend.Model.DB_model import GroupTest
from Backend.DataAccess import get_MS_database, generate_id


class DAO_group_test:
    # SELECT
    def get_group_test_by_group(self, group_id: str) -> list[GroupTest]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [group_test] WHERE [group_id] = %s", (group_id,))
            return [GroupTest(row) for row in cursor.fetchall()]

    def get_group_test_by_id(self, group_test_id: str) -> GroupTest:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [group_test] WHERE [id] = %s", group_test_id)
            row = cursor.fetchone()
            return GroupTest(row) if row else None

    def get_group_test_for_student(self, student_id: str, start: datetime, end: datetime) -> list[GroupTest]:
        with get_MS_database(True) as cursor:
            cursor.execute(
                "SELECT * FROM [group_test] WHERE [group_id] IN (SELECT [group_id] FROM [group_student] WHERE [student_id] = %s) AND CAST([start] AS DATE) >= CAST(%s AS DATE) AND CAST([start] AS DATE) <= CAST(%s AS DATE)",
                (student_id, start, end))
            return [GroupTest(row) for row in cursor.fetchall()]

    # INSERT
    def insert_group_test(self, data: GroupTest) -> str:
        id = generate_id(8)
        failed_count = 0
        with get_MS_database(False) as cursor:
            while True:
                try:
                    cursor.execute(
                        "INSERT INTO [group_test]([id], [group_id], [test_id], [name], [start], [end], [duration], [shuffle], [hash_pswd], [tolerance])  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (id, data.group_id, data.test_id, data.name, data.start, data.end, data.duration, data.shuffle, data.hash_pswd, data.tolerance))
                    return id
                except pymssql.Error as e:
                    if failed_count == 0 and id not in str(e.args[1]):
                        raise e
                    failed_count += 1
                    if failed_count == 5:
                        raise e
                    id = generate_id(8)

    # UPDATE
    def update_group_test(self, data: GroupTest) -> None:
        with get_MS_database(False) as cursor:
            sql = "UPDATE [group_test] SET "
            placeholder = list()
            values = tuple()
            if data.name is not None:
                placeholder.append("[name] = %s")
                values += (data.name,)
            if data.start is not None:
                placeholder.append("[start] = %s")
                values += (data.start,)
            if data.end is not None:
                placeholder.append("[end] = %s")
                values += (data.end,)
            if data.duration is not None:
                placeholder.append("[duration] = %s")
                values += (data.duration,)
            if data.shuffle is not None:
                placeholder.append("[shuffle] = %s")
                values += (data.shuffle,)
            if data.tolerance is not None:
                placeholder.append("[tolerance] = %s")
                values += (data.tolerance,)
            if data.hash_pswd is not None:
                placeholder.append("[hash_pswd] = %s")
                values += (data.hash_pswd,)

            if len(placeholder) == 0:
                return

            sql += ",".join(placeholder) + " WHERE [id] = %s"
            values += (data.id,)
            cursor.execute(sql, values)

    # DELETE
    def delete_group_test(self, group_test_id: str) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("DELETE FROM [group_test] WHERE [id] = %s", (group_test_id,))
