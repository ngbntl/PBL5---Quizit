from Backend.Model.DB_model import Collection
from Backend.DataAccess.DAO_collection import DAO_collection
from Backend.Model.request_model import Req_Collection


class BO_collection:
    def __init__(self):
        self._dao_collection = DAO_collection()

    @property
    def dao_collection(self) -> DAO_collection:
        if self._dao_collection is None:
            self._dao_collection = DAO_collection()
        return self._dao_collection

    # SELECT
    def get_collections_by_teacher(self, teacher_id: str) -> list[Collection]:
        return self.dao_collection.get_collections_by_teacher(teacher_id)

    def get_collection_by_id(self, collection_id) -> Collection:
        return self.dao_collection.get_collection_by_id(collection_id)

    # INSERT
    def insert_collection(self, teacher_id: str, data: Req_Collection) -> str:
        return self.dao_collection.insert_collection(teacher_id=teacher_id, name=data.name)

    # UPDATE
    def update_collection(self, teacher_id: str, data: Req_Collection):
        if self.dao_collection.check_owner(collection_id=data.id, teacher_id=teacher_id) is False:
            raise Exception(f"Collection {data.id} is not belong to teacher {teacher_id}!")
        if data.name is not None:
            self.dao_collection.update_name(id=data.id, name=data.name)

    def delete_collection(self, teacher_id: str, data: Req_Collection):
        if self.dao_collection.check_owner(collection_id=data.id, teacher_id=teacher_id) is False:
            raise Exception(f"Collection {data.id} is not belong to teacher {teacher_id}!")
        if data.name is not None:
            self.dao_collection.delete_collection(id=data.id)
