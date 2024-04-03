from . import get_database
from ..Model.db_model import Collection


class collection_DA:
    # SELECT
    def get_collections_by_teacher(self, teacher_id: str) -> list[Collection] | list | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [collection] WHERE [teacher_id]=%s", teacher_id)
            return [Collection(row) for row in cursor.fetchall()]

    # INSERT
    def insert_collection(self, teacher_id: str, name: str) -> str:
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [collection]([teacher_id], [name])  VALUES (%s, %s)",
                           (teacher_id, name))
        return cursor.lastrowid

    # UPDATE
    def update_collection_name(self, collection_id: str, name: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [collection] SET [name]=%s WHERE [id]=%s", (name, collection_id))
