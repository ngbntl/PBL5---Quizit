from Backend.Model.DB_model import GroupTest


class Room_GroupTest:
    def __init__(self, id: str):
        self.id = id
        self.students = []
        self.group_Test: GroupTest = None