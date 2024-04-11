from Backend.DataAccess import get_database, generate_id


class question_bank_DA:
    # SELECT
    def get_question_banks_by_collection(self, collection_id: str) -> list[dict]:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [question_bank] WHERE [collection_id] = %s", (collection_id,))
            return cursor.fetchall()

    # INSERT
    def insert_question_bank(self, collection_id: str, name: str) -> str:
        failed_count = 0
        with get_database(True) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [question_bank] ([id], [collection_id], [name]) VALUES (%s, %s, %s)", (id, collection_id, name))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count > 5:
                        raise e

    # UPDATE
    def update_question_bank(self, question_bank_id: str, name: str):
        with get_database(True) as cursor:
            cursor.execute("UPDATE [question_bank] SET [name] = %s WHERE [id] = %s", (name, question_bank_id))
