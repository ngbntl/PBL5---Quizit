from Backend.DataAccess.DAO_collection import DAO_collection
from Backend.DataAccess.DAO_test import DAO_test
from Backend.Model.DB_model import Test
from Backend.Model.request_model import Req_Test


class BO_test:
    def __init__(self):
        self._dao_test = None
        self._dao_collection = None

    @property
    def dao_test(self) -> DAO_test:
        if self._dao_test is None:
            self._dao_test = DAO_test()
        return self._dao_test

    @property
    def dao_collection(self) -> DAO_collection:
        if self._dao_collection is None:
            self._dao_collection = DAO_collection()
        return self._dao_collection

    # SELECT
    def get_test_by_collection(self, collection_id: str) -> list[Test]:
        return self.dao_test.get_test_by_collection(collection_id)

    # INSERT
    def insert_test(self, teacher_id: str, data: Req_Test) -> str:
        if self.dao_collection.check_owner(data.collection_id, teacher_id) is False:
            raise ValueError(f"The teacher {teacher_id} is not the owner of the collection {data.collection_id}!")
        return self.dao_test.insert_test(Test(data.model_dump(exclude_unset=True)))
