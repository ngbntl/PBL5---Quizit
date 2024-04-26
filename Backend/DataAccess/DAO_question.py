from Backend.DataAccess import get_MS_database, generate_id
from Backend.Model.DB_model import Question


class DAO_question:
    # INSERT
    def insert_question(self, question: Question) -> str:
        with get_MS_database(True) as cursor:
            failed_count = 0
            while True:
                id = generate_id(10)
                try:
                    cursor.execute(
                        "SELECT ISNULL(MAX([order_number]) + 1, -32768) AS NEXT_ID FROM [question] WHERE [question_bank_id] = %s",
                        question.question_bank_id)
                    next_order_number = cursor.fetchone()['NEXT_ID']
                    cursor.execute(
                        "INSERT INTO [question] ([id], [order_number], [question_bank_id], [content], [answer], [difficulty]) VALUES (%s, %s, %s, %s, %s, %s)",
                        (id, next_order_number, question.question_bank_id, question.content, question.answer,
                         question.difficulty))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    def insert_questions(self, question_bank_id: str, data: list[Question]) -> list[str]:
        with get_MS_database(True) as cursor:
            failed_count = 0
            while True:
                try:
                    cursor.execute(
                        "SELECT ISNULL(MAX([order_number]) + 1, -32768) AS NEXT_ID FROM [question] WHERE [question_bank_id] = %s",
                        question_bank_id)
                    next_order_number = cursor.fetchone()['NEXT_ID']
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

    # SELECT
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

    def count_questions_in_bank(self, question_bank_id: str):
        with get_MS_database(False) as cursor:
            cursor.execute("SELECT COUNT(*) FROM [question] WHERE [question_bank_id] = %s", question_bank_id)
            return cursor.fetchone()[0]

    # UPDATE
    def update_questions(self, question_bank_id: str, data: list[Question]):
        update_content_sql = "UPDATE [question] SET [content] = %s WHERE [question_bank_id] = %s AND [id] = %s"
        update_difficulty_sql = "UPDATE [question] SET [difficulty] = %s WHERE [question_bank_id] = %s AND [id] = %s"
        update_answer_sql = "UPDATE [question] SET [answer] = %s WHERE [question_bank_id] = %s AND [id] = %s"
        with get_MS_database(True) as cursor:
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

    # DELETE
    def delete_questions(self, question_bank_id: str, question_ids: list[str]):
        with get_MS_database(True) as cursor:
            try:
                cursor.execute("DELETE FROM [question] WHERE [question_bank_id] = %s AND [id] IN %s",
                               (question_bank_id, tuple(question_ids)))
                return
            except Exception as e:
                raise e

    def delete_question(self, question_bank_id: str, question_id: str):
        with get_MS_database(True) as cursor:
            try:
                cursor.execute("DELETE FROM [question] WHERE [question_bank_id] = %s AND [id] = %s",
                               (question_bank_id, question_id))
                return
            except Exception as e:
                raise e
