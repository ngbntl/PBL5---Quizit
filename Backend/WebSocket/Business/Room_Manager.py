from Backend.WebSocket.Business import singleton
from Backend.WebSocket.Entity.Room_GroupTest import Room_GroupTest


@singleton
class Room_Manager:
    def __init__(self):
        self.room_group_test: dict[Room_GroupTest] = dict()

    def is_room_exist(self, group_test_id: str):
        return group_test_id in self.room_group_test.keys()

    def add_room(self, group_test_id: str, room: Room_GroupTest):
        self.room_group_test[group_test_id] = room

    def get_room_hash_password(self, group_test_id: str) -> str:
        return self.room_group_test[group_test_id].hash_pswd

    def set_room_hash_password(self, group_test_id: str, value: str):
        self.room_group_test[group_test_id].hash_pswd = value

    def get_room(self, group_test_id: str) -> Room_GroupTest:
        return self.room_group_test.get(group_test_id, None)
