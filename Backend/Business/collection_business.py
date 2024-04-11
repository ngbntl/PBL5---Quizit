from Backend.Model.response_model import Res_Collection
from Backend.DataAccess.collection_DA import collection_DA
from Backend.Model.request_model import Req_Collection


class collection_business:
    def __init__(self):
        self.collection_DA = collection_DA()

    # SELECT
    def get_collections_by_teacher(self, teacher_id: str) -> list[dict]:
        return self.collection_DA.get_collections_by_teacher(teacher_id)

    def get_collection_by_id(self, collection_id) -> dict | None:
        return self.collection_DA.get_collection_by_id(collection_id)

    # INSERT
    def insert_collection(self, teacher_id: str, data: Req_Collection) -> str:
        data.teacher_id = teacher_id
        return self.collection_DA.insert_collection(data)

    # UPDATE
    def update_collection(self, teacher_id: str, data: Req_Collection):
        data.teacher_id = teacher_id
        if (name := data.name) is not None:
            self.update_collection_name(data.id, name)

    def update_collection_name(self, collection_id: str, name: str):
        self.collection_DA.update_collection_name(collection_id, name)
