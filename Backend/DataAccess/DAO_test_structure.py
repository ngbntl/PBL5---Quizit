import pickle

from Backend.DataAccess import get_MS_database
from Backend.Model.DB_model import TestStructure


class DAO_test_structure:
    # INSERT
    def insert_structure(self, data: TestStructure):
        if data.test_id is None:
            raise ValueError("The test_id is required!")
        if data.question_bank_id is None:
            raise ValueError("The question_bank_id is required!")
        if data.number_of_question is None:
            raise ValueError("The number_of_question is required!")

        with get_MS_database(False) as cursor:
            cursor.execute(
                "INSERT INTO [test_structure] ([test_id], [question_bank_id], [number_of_question]) VALUES (%s, %s, %s)",
                (data.test_id, data.question_bank_id, pickle.dumps(data.number_of_question)))

    # SELECT
    def get_structure(self, test_id: str) -> list[TestStructure]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [test_structure] WHERE [test_id] = %s", (test_id,))
            return [TestStructure(ts) for ts in cursor.fetchall()]

    # UPDATE
    def update_structure(self, data: TestStructure):
        with get_MS_database(False) as cursor:
            cursor.execute(
                "UPDATE [test_structure] SET [number_of_question] = %s WHERE [test_id] = %s AND [question_bank_id] = %s",
                (pickle.dumps(data.number_of_question), data.test_id, data.question_bank_id))
