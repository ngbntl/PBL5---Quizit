from Backend.DataAccess import get_MS_database
from Backend.Model.DB_model import Group, Student


class DAO_group_student:
    # SELECT
    def get_students_by_group(self, group_id: str, is_join: bool = True) -> list[Student]:
        with get_MS_database(True) as cursor:
            cursor.execute("""
                SELECT * FROM [student] WHERE [id] IN 
                (SELECT [student_id] from [group_student] WHERE [group_id] = %s AND [is_join] = %s)
            """, (group_id, is_join))
            return [Student(record) for record in cursor.fetchall()]

    def get_group_id_by_student(self, student_id: str, is_join: bool = True) -> list[str]:
        with get_MS_database(False) as cursor:
            cursor.execute("SELECT [group_id] FROM [group_student] WHERE [student_id] = %s AND [is_join] = %s",
                           (student_id, is_join))
            return [record[0] for record in cursor.fetchall()]

    def get_groups_by_student(self, student_id, is_join) -> list[Group]:
        with get_MS_database(True) as cursor:
            cursor.execute("""
                SELECT * FROM [group] WHERE [id] IN 
                (SELECT [group_id] FROM [group_student] WHERE [student_id] = %s AND [is_join] = %s)
            """, (student_id, is_join))
            return [Group(record) for record in cursor.fetchall()]

    # INSERT
    def request_join(self, group_id: str, student_id: str) -> None:
        with get_MS_database(False) as cursor:
            try:
                cursor.execute("INSERT INTO [group_student]([group_id], [student_id], [is_join]) VALUES (%s, %s, 0)",
                               (group_id, student_id))
            except:
                cursor.execute("UPDATE [group_student] SET [is_join] = 1 WHERE [group_id] = %s AND [student_id] = %s",
                               (group_id, student_id))

    def insert_students(self, group_id: str, list_id: list[str]) -> None:
        self.delete_students(group_id, list_id)
        with get_MS_database(False) as cursor:
            query = f"INSERT INTO [group_student]([group_id], [student_id], [is_join]) VALUES ('{group_id}', %s, 1)"
            for student_id in list_id:
                try:
                    cursor.execute(query, student_id)
                except Exception as e:
                    raise e

    # UPDATE
    # def update_join_requests(self, group_id: str, student_id: str, accept: bool) -> None:
    #     with get_MS_database(True) as cursor:
    #         cursor.execute("UPDATE [group_student] SET [is_join] = %s WHERE [group_id] = %s AND [student_id] = %s",
    #                        (accept, group_id, student_id))

    def update_visibility(self, group_id: str, student_id: str, visibility: bool) -> None:
        with get_MS_database(False) as cursor:
            cursor.execute("UPDATE [group_student] SET [is_show] = %s WHERE [group_id] = %s AND [student_id] = %s",
                           (visibility, group_id, student_id))

    # DELETE

    def delete_student(self, group_id, student_id):
        with get_MS_database(False) as cursor:
            cursor.execute("DELETE FROM [group_student] WHERE [group_id] = %s AND [student_id] = %s",
                           (group_id, student_id))

    def delete_students(self, group_id: str, list_id: list[str]):
        list_id = tuple(list_id)  # Convert list_id to tuple
        with get_MS_database(False) as cursor:
            placeholders = ','.join(['%s'] * len(list_id))
            query = f"DELETE FROM [group_student] WHERE [group_id] = %s AND [student_id] IN ({placeholders})"
            params = (group_id,) + list_id
            cursor.execute(query, params)
