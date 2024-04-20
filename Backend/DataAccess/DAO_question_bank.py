from Backend.DataAccess import get_MS_database, DAO_test
from Backend.Model.DB_model import QuestionBank


class DAO_question_bank:
    # SELECT
    def get_question_banks_by_collection(self, collection_id: str) -> list[QuestionBank]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [question_bank] WHERE [collection_id] = %s", (collection_id,))
            return [QuestionBank(row) for row in cursor.fetchall()]

    def get_collection_id(self, question_bank_id) -> str:
        with get_MS_database(False) as cursor:
            cursor.execute("SELECT [collection_id] FROM [question_bank] WHERE [id] = %s", question_bank_id)
            return cursor.fetchone()[0]

    # INSERT
    def insert_question_bank(self, collection_id: str, name: str) -> str:
        with get_MS_database(True) as cursor:
            failed_count = 0
            while True:
                id = DAO_test(8)
                try:
                    cursor.execute("INSERT INTO [question_bank] ([id], [collection_id], [name]) VALUES (%s, %s, %s)",
                                   (id, collection_id, name))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    # UPDATE
    def update_name(self, question_bank_id: str, name: str):
        with get_MS_database(True) as cursor:
            cursor.execute("UPDATE [question_bank] SET [name] = %s WHERE [id] = %s", (name, question_bank_id))
