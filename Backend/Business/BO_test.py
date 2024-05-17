import pickle
from typing import Generator

from Backend.DataAccess.DAO_collection import DAO_collection
from Backend.DataAccess.DAO_test import DAO_test
from Backend.DataAccess.DAO_test_structure import DAO_test_structure
from Backend.Model.DB_model import Test, TestStructure
from Backend.Model.request_model import Req_Test
from Backend.Model.response_model import Res_Test, Res_TestStructure


class BO_test:
    def __init__(self):
        self._dao_test = None
        self._dao_collection = None
        self._dao_test_structure = None

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

    @property
    def dao_test_structure(self) -> DAO_test_structure:
        if self._dao_test_structure is None:
            self._dao_test_structure = DAO_test_structure()
        return self._dao_test_structure

    # SELECT
    def get_test_by_collection(self, collection_id: str, teacher_id=None) -> Generator[Res_Test, None, None]:
        if teacher_id is not None and self.dao_collection.check_owner(collection_id, teacher_id) is False:
            raise ValueError(f"The teacher {teacher_id} is not the owner of the collection {collection_id}!")
        for test in self.dao_test.get_test_by_collection(collection_id):
            restest = Res_Test(id=test.id, collection_id=test.collection_id, name=test.name,
                               created_timestamp=test.created_timestamp, structure=[])

            restest.structure.extend(
                Res_TestStructure(test_id=test.id, question_bank_id=s.question_bank_id,
                                  number_of_question=pickle.loads(s.number_of_question))
                for s in self.dao_test_structure.get_structure(test.id)
            )
            yield restest

    # INSERT
    def insert_test(self, teacher_id: str, data: Req_Test) -> str:
        if self.dao_collection.check_owner(data.collection_id, teacher_id) is False:
            raise ValueError(f"The teacher {teacher_id} is not the owner of the collection {data.collection_id}!")
        test_id = self.dao_test.insert_test(Test(data.model_dump(exclude_unset=True)))
        for structure in data.structure:
            self.dao_test_structure.insert_structure(TestStructure(
                {'test_id': test_id, 'question_bank_id': structure.question_bank_id,
                 'number_of_question': pickle.dumps([noq.model_dump() for noq in structure.number_of_question])}))
        return test_id
