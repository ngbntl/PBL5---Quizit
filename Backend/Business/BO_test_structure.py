import pickle

from Backend.DataAccess.DAO_test import DAO_test
from Backend.DataAccess.DAO_test_structure import DAO_test_structure
from Backend.Model.DB_model import TestStructure
from Backend.Model.request_model import Req_TestStructure
from Backend.Model.response_model import Res_TestStructure


class BO_test_structure:
    def __init__(self):
        self._dao_test_structure = None
        self._dao_test = None

    @property
    def dao_test_structure(self) -> DAO_test_structure:
        if self._dao_test_structure is None:
            self._dao_test_structure = DAO_test_structure()
        return self._dao_test_structure

    @property
    def dao_test(self) -> DAO_test:
        if self._dao_test is None:
            self._dao_test = DAO_test()
        return self._dao_test

    # INSERT
    def insert_structure(self, teacher_id: str, data: Req_TestStructure) -> None:
        if self.dao_test.check_owner(test_id=data.test_id, teacher_id=teacher_id) is False:
            raise Exception(f"The test with id {data.test_id} is not owned by teacher with id {teacher_id}")
        self.dao_test_structure.insert_structure(TestStructure(
            {'test_id': data.test_id, 'question_bank_id': data.question_bank_id,
             'number_of_question': pickle.dumps([noq.model_dump() for noq in data.number_of_question])}))

    # SELECT
    def get_structure(self, test_id: str) -> list[Res_TestStructure]:
        # return [Res_TestStructure(test_id=test_id, question_bank_id=ts.question_bank_id, number_of_question=pickle.loads(ts.number_of_question)) for ts in self.dao_test_structure.get_structure(test_id)]
        arr = []
        for ts in self.dao_test_structure.get_structure(test_id):
            number_of_question = pickle.loads(ts.number_of_question)
            print(number_of_question)
            arr.append(Res_TestStructure(test_id=test_id, question_bank_id=ts.question_bank_id,
                                         number_of_question=number_of_question))
        return arr

    # UPDATE
    def update_structure(self, teacher_id: str, data: Req_TestStructure):
        if self.dao_test.check_owner(test_id=data.test_id, teacher_id=teacher_id):
            raise Exception(f"The test with id {data.test_id} is not owned by teacher with id {teacher_id}")
        self.dao_test_structure.update_structure(TestStructure(
            {'test_id': data.test_id, 'question_bank_id': data.question_bank_id,
             'number_of_question': pickle.dumps([noq.model_dump() for noq in data.number_of_question])}))
