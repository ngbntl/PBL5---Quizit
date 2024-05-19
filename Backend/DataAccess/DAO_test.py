import pickle

import pymssql

from Backend.DataAccess import get_MS_database, generate_id
from Backend.Model.DB_model import Test


class DAO_test:
    # SELECT
    def get_test_by_collection(self, collection_id: str) -> list[Test]:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [test] WHERE [collection_id]=%s", collection_id)
            return [Test(t) for t in cursor.fetchall()]

    def check_owner(self, test_id: str, teacher_id: str) -> bool:
        SQL = "SELECT * FROM [test] JOIN [collection] ON [test].[collection_id]=[collection].[id] WHERE [test].[id]=%s AND [collection].[teacher_id]=%s"
        with get_MS_database(False) as cursor:
            cursor.execute(SQL, (test_id, teacher_id))
            return cursor.fetchone() is not None

    def get_test_by_id(self, test_id: str) -> Test:
        with get_MS_database(True) as cursor:
            cursor.execute("SELECT * FROM [test] WHERE [id]=%s", test_id)
            return Test(cursor.fetchone())

    # INSERT
    def insert_test(self, data: Test) -> str:
        if data.collection_id is None:
            raise ValueError("The collection_id is required!")
        if data.name is None:
            raise ValueError("The name is required!")
        if data.structure is None:
            raise ValueError("The structure is required!")

        failed_count = 0
        with get_MS_database(False) as cursor:
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [test] ([id], [collection_id], [name]) VALUES (%s, %s, %s)",
                                   (id, data.collection_id, data.name))
                    cursor.executemany(
                        "INSERT INTO [test_structure] ([test_id], [question_bank_id], [number_of_question]) VALUES (%s, %s, %s)",
                        [(id, ts.question_bank_id, pickle.dumps(ts.number_of_question)) for ts in data.structure])
                    return id
                except pymssql.Error as e:
                    if failed_count == 0 and id not in str(e.args[1]):
                        raise e
                    failed_count += 1
                    if failed_count == 5:
                        raise e

    # UPDATE
    def update_test_name(self, data: Test) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [test] SET [name]=%s WHERE [id]=%s", (data.name, data.id))
