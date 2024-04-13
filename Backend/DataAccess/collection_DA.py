from Backend.DataAccess import get_database, generate_id
from Backend.Model.request_model import Req_Collection


class collection_DA:
    # SELECT
    def get_collections_by_teacher(self, teacher_id: str) -> list[dict]:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [collection] WHERE [teacher_id]=%s", teacher_id)
            return cursor.fetchall()

    def get_collection_by_id(self, collection_id) -> dict | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [collection] WHERE [id]=%s", collection_id)
            return cursor.fetchone()

    def check_owner(self, collection_id: str, teacher_id: str) -> bool:
        with get_database(False) as cursor:
            cursor.execute("SELECT [id] FROM [collection] WHERE [id]=%s AND [teacher_id]=%s", (collection_id, teacher_id))
            return cursor.fetchone() is not None

    # INSERT
    def insert_collection(self, data: Req_Collection) -> str:

        with get_database(True) as cursor:
            failed_count = 0
            while True:
                id = generate_id(8)
                try:
                    cursor.execute("INSERT INTO [collection] ([id], [name], [teacher_id]) VALUES (%s, %s, %s)",
                                   (id, data.name, data.teacher_id))
                    return id
                except Exception as e:
                    failed_count += 1
                    if failed_count > 5:
                        raise e

    # UPDATE
    def update_collection_name(self, collection_id: str, name: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [collection] SET [name]=%s WHERE [id]=%s", (name, collection_id))
