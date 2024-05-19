import pymssql

from Backend.DataAccess import get_MS_database, generate_id
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

    def check_owner(self, teacher_id: str, question_bank_id: str) -> bool:
        collection_id = self.get_collection_id(question_bank_id)
        with get_MS_database(False) as cursor:
            cursor.execute("SELECT [id] FROM [collection] WHERE [teacher_id] = %s AND [id] = %s",
                           (teacher_id, collection_id))
            return cursor.fetchone() is not None

    # INSERT
    def insert_question_bank(self, question_bank: QuestionBank) -> str:
        with get_MS_database(False) as cursor:
            failed_count = 0
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [question_bank] ([id], [collection_id], [name]) VALUES (%s, %s, %s)",
                                   (id, question_bank.collection_id, question_bank.name))
                    return id
                except pymssql.Error as e:
                    if failed_count == 0 and id not in str(e.args[1]):
                        raise e
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    # UPDATE
    def update(self, question_bank: QuestionBank):
        with get_MS_database(False) as cursor:
            sql = "UPDATE [question_bank] SET "
            placeholder = list()
            values = tuple()
            if question_bank.name is not None:
                placeholder.append("[name] = %s")
                values += (question_bank.name,)
            if len(placeholder) == 0:
                return
            sql += ",".join(placeholder) + " WHERE [id] = %s"
            values += (question_bank.id,)
            cursor.execute(sql, values)
