from Backend.DataAccess import get_database, generate_id
from Backend.Model.request_model import Req_GenerateTest


class generate_test_DA:
    # SELECT
    def get_generate_tests_by_collection(self, collection_id: str) -> list[dict] | list | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [generate_test] WHERE [collection_id]=%s", collection_id)
            return cursor.fetchall()

    # INSERT
    def insert_generate_test(self, data: Req_GenerateTest) -> str:
        failed_count = 0
        with get_database(True) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [generate_test] ([id], [collection_id], [name]) VALUES (%s, %s, %s)",
                                   (id, data.collection_id, data.name))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count > 5:
                        raise e

    # UPDATE
    def update_generate_test_name(self, test_id: str, name: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [generate_test] SET [name]=%s WHERE [id]=%s", (name, test_id))
