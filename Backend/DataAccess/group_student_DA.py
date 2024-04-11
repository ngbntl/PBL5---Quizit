from Backend.DataAccess import get_database


class group_student_DA:
    # SELECT
    def get_students_by_group(self, group_id: str, is_join: bool = True) -> list[str]:
        with get_database(False) as cursor:
            cursor.execute("SELECT [student_id] WHERE [group_id] = %s AND [is_join] = %s", (group_id, is_join))
            return cursor.fetchall()

    def get_group_id_by_student(self, student_id: str, is_join: bool = True) -> list[str]:
        with get_database(False) as cursor:
            cursor.execute("SELECT [group_id] FROM [group_student] WHERE [student_id] = %s AND [is_join] = %s",
                           (student_id, is_join))
            return [record[0] for record in cursor.fetchall()]

    def get_groups_by_student(self, student_id, is_join):
        with get_database(True) as cursor:
            cursor.execute("""
                SELECT * FROM [group] WHERE [id] IN 
                (SELECT [group_id] FROM [group_student] WHERE [student_id] = %s AND [is_join] = %s)
            """, (student_id, is_join))
            return cursor.fetchall()

    # INSERT
    def insert_student(self, group_id: str, student_id: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [group_student]([group_id], [student_id])  VALUES (%s, %s)",
                           (group_id, student_id))

    # UPDATE
    def accept_join_request(self, group_id: str, student_id: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [group_student] SET [is_join] = 1 WHERE [group_id] = %s AND [student_id] = %s",
                           (group_id, student_id))

    def update_visibility(self, group_id: str, student_id: str, visibility: bool) -> None:
        with get_database(True) as cursor:
            cursor.execute("UPDATE [group_student] SET [is_show] = %s WHERE [group_id] = %s AND [student_id] = %s",
                           (visibility, group_id, student_id))
    # DELETE

    def delete_join_request(self, group_id: str, student_id: str) -> None:
        with get_database(True) as cursor:
            cursor.execute("DELETE FROM [group_student] WHERE [group_id] = %s AND [student_id] = %s",
                           (group_id, student_id))
