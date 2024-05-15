import pickle

import pymssql

from Backend.DataAccess import get_MS_database, generate_id
from Backend.Model.DB_model import Question, QuestionBank
from Backend.Model.response_model import Res_NumberOfQuestion


class DAO_question:
    # INSERT
    def insert_question(self, question: Question) -> str:
        with get_MS_database(False) as cursor:
            failed_count = 0
            while True:
                id = generate_id(10)
                try:
                    cursor.execute(
                        "SELECT ISNULL(MAX([order_number]) + 1, -32768) FROM [question] WHERE [question_bank_id] = %s",
                        question.question_bank_id)
                    next_order_number = cursor.fetchone()[0]
                    cursor.execute(
                        "INSERT INTO [question] ([id], [order_number], [question_bank_id], [content], [answer], [difficulty]) VALUES (%s, %s, %s, %s, %s, %s)",
                        (id, next_order_number, question.question_bank_id, question.content, question.answer,
                         question.difficulty))
                    return id
                except pymssql.Error as e:
                    if failed_count == 0 and id not in str(e.args[1]):
                        raise e
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    def insert_questions(self, question_bank_id: str, data: list[Question]) -> list[str]:
        with get_MS_database(False) as cursor:
            failed_count = 0
            while True:
                try:
                    cursor.execute(
                        "SELECT ISNULL(MAX([order_number]) + 1, -32768) FROM [question] WHERE [question_bank_id] = %s",
                        question_bank_id)
                    next_order_number = cursor.fetchone()[0]
                    statement = "INSERT INTO [question] ([id], [order_number], [question_bank_id], [content], [answer], [difficulty]) VALUES (%s, %s, %s, %s, %s, %s)"
                    seq_of_parameters = [
                        (generate_id(10), next_order_number + i, question_bank_id, q.content, q.answer, q.difficulty)
                        for i, q in enumerate(data)]
                    cursor.executemany(statement, seq_of_parameters)
                    return [t[0] for t in seq_of_parameters]
                except Exception as e:
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    async def insert_attachment_path(self, question_id: str, attachment_path: list[str]):
        with get_MS_database(False) as cursor:
            cursor.execute("SELECT [attachment] FROM [question] WHERE [id] = %s", question_id)
            attachment = cursor.fetchone()[0]
            if attachment is None:
                attachment = []
            else:
                attachment = pickle.loads(attachment)
            attachment.extend(attachment_path)
            cursor.execute("UPDATE [question] SET [attachment] = %s WHERE [id] = %s",
                           (pickle.dumps(attachment), question_id))

    # SELECT
    def get_question_by_id(self, question_id: str) -> Question:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [question] WHERE [id] = %s", question_id)
            q = cursor.fetchone()
            if q is None:
                return None
            return Question(q)

    def get_questions_in_bank(self, question_bank_id: str, offset: int, length: int) -> list[Question]:
        with get_MS_database(True) as cursor:
            sql = """
            WITH NumberedRows AS (
                SELECT *, ROW_NUMBER() OVER (ORDER BY [order_number]) AS RowNum
                FROM [question] WHERE [question_bank_id] = %s
            )
        SELECT *
        FROM NumberedRows
        WHERE RowNum BETWEEN %s AND %s
            """
            cursor.execute(sql, (question_bank_id, offset, offset + length - 1))
            return [Question(q) for q in cursor.fetchall()]

    def get_questions_in_bank_by_difficulty(self, question_bank_id: str, difficulty: int, number: int, shuffle: bool = False) -> list[Question]:
        with get_MS_database(True) as cursor:
            sql = """
            SELECT TOP(%s) *
            FROM [question]
            WHERE [question_bank_id] = %s AND [difficulty] = %s
            """
            if shuffle:
                sql += " ORDER BY NEWID()"
            cursor.execute(sql, (number, question_bank_id, difficulty))
            return [Question(q) for q in cursor.fetchall()]

    def summary(self, question_bank_id: str) -> list[Res_NumberOfQuestion]:
        with get_MS_database(True) as cursor:
            sql = "SELECT [difficulty], COUNT(*) as [number_of_question] FROM [question] WHERE [question_bank_id] = %s GROUP BY [difficulty]"
            cursor.execute(sql, question_bank_id)
            return [Res_NumberOfQuestion(**q) for q in cursor.fetchall()]

    def get_question_bank(self, question_id: str):
        with get_MS_database(True) as cursor:
            cursor.execute(
                "SELECT * FROM [question_bank] WHERE [id] IN (SELECT [question_bank_id] FROM [question] WHERE [id] = %s)",
                question_id)
            q = cursor.fetchone()
            if q is None:
                return None
            return QuestionBank(q)

    def check_owner(self, teacher_id: str, question_id: str) -> bool:
        with get_MS_database(False) as cursor:
            sql = """
            SELECT c.[id] 
            FROM [collection] c
            JOIN [question_bank] qb ON c.[id] = qb.[collection_id]
            JOIN [question] q ON qb.[id] = q.[question_bank_id]
            WHERE c.[teacher_id] = %s AND q.[id] = %s
            """
            cursor.execute(sql, (teacher_id, question_id))
            return cursor.fetchone() is not None

    # UPDATE
    def update_questions(self, question_bank_id: str, data: list[Question]):
        update_content_sql = "UPDATE [question] SET [content] = %s WHERE [question_bank_id] = %s AND [id] = %s"
        update_difficulty_sql = "UPDATE [question] SET [difficulty] = %s WHERE [question_bank_id] = %s AND [id] = %s"
        update_answer_sql = "UPDATE [question] SET [answer] = %s WHERE [question_bank_id] = %s AND [id] = %s"
        with get_MS_database(False) as cursor:
            for q in data:
                try:
                    if q.id is None:
                        continue
                    if q.content is not None:
                        cursor.execute(update_content_sql, (q.content, question_bank_id, q.id))
                    if q.difficulty is not None:
                        cursor.execute(update_difficulty_sql, (q.difficulty, question_bank_id, q.id))
                    if q.answer is not None:
                        cursor.execute(update_answer_sql, (q.answer, question_bank_id, q.id))
                except Exception as e:
                    raise e

    def update_question_attachment(self, question: Question):
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [question] SET [attachment] = %s WHERE [id] = %s",
                           (question.attachment, question.id))

    # DELETE
    def delete_questions(self, question_bank_id: str, question_ids: list[str]):
        with get_MS_database(False) as cursor:
            try:
                cursor.execute("DELETE FROM [question] WHERE [question_bank_id] = %s AND [id] IN %s",
                               (question_bank_id, tuple(question_ids)))
                return
            except Exception as e:
                raise e

    def delete_question(self, question_bank_id: str, question_id: str):
        with get_MS_database(False) as cursor:
            try:
                cursor.execute("DELETE FROM [question] WHERE [question_bank_id] = %s AND [id] = %s",
                               (question_bank_id, question_id))
                return
            except Exception as e:
                raise e
