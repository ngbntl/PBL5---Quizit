from Backend.DataAccess import get_database, generate_id


class mutual_test_DA:
    # SELECT
    def get_manual_tests_by_collection(self, collection_id: str) -> list[dict]:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [manual_test] WHERE [collection_id]=%s", collection_id)
            return cursor.fetchall()

    # INSERT
    def insert_manual_test(self, collection_id: str, name: str) -> str:
        id = generate_id(8)
        failed_count = 0
        with get_database(True) as cursor:
            while True:
                try:
                    cursor.execute("INSERT INTO [manual_test]([id], [collection_id], [name])  VALUES (%s, %s, %s)",
                                   (id, collection_id, name))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count > 5:
                        raise e
                    id = generate_id(8)

    # UPDATE
    def update_manual_test_name(self, test_id: str, name: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [manual_test] SET [name]=%s WHERE [id]=%s", (name, test_id))
