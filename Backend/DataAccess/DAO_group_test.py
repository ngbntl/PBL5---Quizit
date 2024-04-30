from Backend.DataAccess import get_MS_database, generate_id
from datetime import datetime


class DAO_group_test:
    # SELECT
    def get_all_group_tests(self, group_id: str) -> list[dict]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [group_test] WHERE [group_id] = %s", (group_id,))
            return cursor.fetchall()

    # INSERT
    def insert_group_test(self, group_id: str, test_path: str, start: datetime, end: datetime) -> str:
        id = generate_id(8)
        failed_count = 0
        with get_MS_database(False) as cursor:
            while True:
                try:
                    cursor.execute("INSERT INTO [group_test]([id], [group_id], [test_path], [start], [end])  VALUES (%s, %s, %s, %s, %s)",
                                   (id, group_id, test_path, start, end))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count > 5:
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
