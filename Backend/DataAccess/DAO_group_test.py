from Backend.DataAccess import get_MS_database, generate_id
from datetime import datetime

from Backend.Model.DB_model import GroupTest


class DAO_group_test:
    # SELECT
    def get_group_test(self, group_id: str) -> list[GroupTest]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [group_test] WHERE [group_id] = %s", (group_id,))
            return [GroupTest(row) for row in cursor.fetchall()]

    # INSERT
    def insert_group_test(self, data: GroupTest) -> str:
        id = generate_id(8)
        failed_count = 0
        duplicate_PK = False
        with get_MS_database(False) as cursor:
            while True:
                try:
                    cursor.execute(
                        "INSERT INTO [group_test]([id], [group_id], [test_id], [start], [end], [duration], [shuffle])  VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (id, data.group_id, data.test_id, data.start, data.end, data.duration, data.shuffle))
                    return id
                except Exception as e:
                    if duplicate_PK is False and id not in str(e.args[1]):
                        raise e  # Another error. Not duplicate id
                    duplicate_PK = True  # Not athor error. Duplicate id
                    failed_count += 1
                    if failed_count == 5:
                        raise e
                    id = generate_id(8)

    # UPDATE
    def update_time(self, group_test_id: str, star: datetime, end: datetime) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [group_test] SET [start] = %s, [end] = %s WHERE [id] = %s",
                           (star, end, group_test_id))

    # DELETE
    def delete_group_test(self, group_test_id: str) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("DELETE FROM [group_test] WHERE [id] = %s", (group_test_id,))
