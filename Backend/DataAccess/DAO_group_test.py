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
                "SELECT * FROM [group_test] WHERE [group_id] IN (SELECT [group_id] FROM [group_student] WHERE [student_id] = %s) AND [start] >= %s AND [start] <= %s",
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
                        "INSERT INTO [group_test]([id], [group_id], [test_id], [name], [start], [end], [duration], [shuffle])  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (id, data.group_id, data.test_id, data.name, data.start, data.end, data.duration, data.shuffle))
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
            cursor.execute(
                "UPDATE [group_test] SET [start]=%s, [end]=%s, [duration]=%s, [shuffle]=%s WHERE [id]=%s",
                (data.start, data.end, data.duration, data.shuffle, data.id))

    # DELETE
    def delete_group_test(self, group_test_id: str) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("DELETE FROM [group_test] WHERE [id] = %s", (group_test_id,))
