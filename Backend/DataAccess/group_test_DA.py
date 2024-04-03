from Backend.DataAccess import get_database
from datetime import datetime


class group_test_DA:
    # SELECT


    # INSERT
    def insert_group_test(self, group_id: str, test_path: str, start: datetime, end: datetime) -> None:
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [group_test]([group_id], [test_path], [start], [end])  VALUES (%s, %s, %s, %s)",
                           (group_id, test_path, start, end))

