from . import get_database
from ..Model.db_model import GenerateTest


class collection_DA:
    # SELECT
    def get_generate_tests_by_collection(self, collection_id: str) -> list[GenerateTest] | list | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [generate_test] WHERE [collection_id]=%s", collection_id)
            return [GenerateTest(row) for row in cursor.fetchall()]

    # INSERT
    def insert_generate_test(self, collection_id: str, name: str) -> str:
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [generate_test]([collection_id], [name])  VALUES (%s, %s)",
                           (collection_id, name))
        return cursor.lastrowid

    # UPDATE
    def update_generate_test_name(self, test_id: str, name: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [generate_test] SET [name]=%s WHERE [id]=%s", (name, test_id))
