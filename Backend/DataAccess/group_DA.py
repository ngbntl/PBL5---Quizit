class group_DA:
    def insert_group(self, teacher_id: str, name: str) -> str:
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [group]([teacher_id], [name])  VALUES (%s, %s)", (teacher_id, name))
            return cursor.lastrowid