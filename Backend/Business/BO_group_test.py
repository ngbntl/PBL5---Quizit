from Backend.DataAccess.DAO_group import DAO_group
from Backend.DataAccess.DAO_group_test import DAO_group_test
from Backend.DataAccess.DAO_question import DAO_question
from Backend.DataAccess.DAO_student_test import DAO_student_test
from Backend.DataAccess.DAO_test import DAO_test
from Backend.DataAccess.DAO_test_structure import DAO_test_structure
from Backend.Model.DB_model import GroupTest, TestStructure, Question, StudentWork_Question, StudentTest
from Backend.Model.request_model import Req_GroupTest
from Backend.Model.response_model import Res_StudentTest


class BO_group_test:
    def __init__(self):
        self._dao_group_test = None
        self._dao_group = None
        self._dao_test = None
        self._dao_test_structure = None
        self._dao_question = None
        self._dao_student_test = None

    @property
    def dao_group_test(self):
        if not self._dao_group_test:
            self._dao_group_test = DAO_group_test()
        return self._dao_group_test

    @property
    def dao_group(self):
        if not self._dao_group:
            self._dao_group = DAO_group()
        return self._dao_group

    @property
    def dao_test(self):
        if not self._dao_test:
            self._dao_test = DAO_test()
        return self._dao_test

    @property
    def dao_test_structure(self):
        if not self._dao_test_structure:
            self._dao_test_structure = DAO_test_structure()
        return self._dao_test_structure

    @property
    def dao_question(self):
        if not self._dao_question:
            self._dao_question = DAO_question()
        return self._dao_question

    @property
    def dao_student_test(self):
        if not self._dao_student_test:
            self._dao_student_test = DAO_student_test()
        return self._dao_student_test

    # INSERT
    def insert_group_test(self, teacher_id: str, data: Req_GroupTest) -> str:
        if self.dao_group.check_owner(data.group_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of group {data.group_id}")
        if data.group_id is None:
            raise Exception("Group id is required")
        if data.test_id is None:
            raise Exception("Test id is required")
        if data.start is None:
            raise Exception("Start time is required")
        if data.end is None:
            raise Exception("End time is required")
        if data.duration is None:
            raise Exception("Duration is required")

        return self.dao_group_test.insert_group_test(data.to_DB_model())

    # SELECT
    def get_group_test_in_group(self, group_id: str) -> list[GroupTest]:
        return self.dao_group_test.get_group_test_by_group(group_id)

    def get_group_test_by_id(self, group_test_id: str) -> GroupTest:
        return self.dao_group_test.get_group_test_by_id(group_test_id)

    def generate_student_work(self, group_test_id: str) -> list[StudentWork_Question]:
        # Get group test by id
        group_test = self.get_group_test_by_id(group_test_id)
        if group_test is None:
            raise Exception(f"Group test {group_test_id} not found")
        student_work_question = []
        # Then get test by id
        test = self.dao_test.get_test_by_id(group_test.test_id)
        # Get test structure
        test_structer: list[TestStructure] = self.dao_test_structure.get_structure(test.id)
        # For each test structure, get the number of question then get the question
        for ts in test_structer:
            for n in ts.number_of_question:  # n: NumberOfQuestion
                # get n.number_of_question questions from question bank ts.question_bank_id with difficulty n.difficulty
                # random order if group_test.shuffle is True
                questions: list[Question] = self.dao_question.get_questions_in_bank_by_difficulty(ts.question_bank_id,
                                                                                                  n.difficulty,
                                                                                                  n.number_of_question,
                                                                                                  group_test.shuffle)
                for q in questions:
                    student_work_question.append(
                        StudentWork_Question(content=q.content, answer=q.answer,
                                             attachment=q.attachment, student_answer=None))
        return student_work_question

    def get_studentworks(self, group_test_id: str) -> list[StudentTest]:
        return self.dao_student_test.get_student_tests(group_test_id)

    def get_studentwork(self, group_test_id: str, student_id: str) -> StudentTest:
        return self.dao_student_test.get_student_test(group_test_id, student_id)

    def get_studentpoints_by_test(self, group_test_id: str) -> list[StudentTest]:
        return self.dao_student_test.get_student_points(group_test_id)

    # UPDATE
    def update_group_test(self, teacher_id: str, data: Req_GroupTest):
        group_test = self.dao_group_test.get_group_test_by_id(data.id)

        if not group_test:
            raise Exception(f"Group test {data.id} not found")

        if self.dao_group.check_owner(group_test.group_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of group {group_test.group_id}")
        if self.dao_test.check_owner(group_test.test_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of test {group_test.test_id}")

        if data.start is not None:
            group_test.start = data.start
        if data.end is not None:
            group_test.end = data.end
        if data.duration is not None:
            group_test.duration = data.duration
        if data.shuffle is not None:
            group_test.shuffle = data.shuffle

        self.dao_group_test.update_group_test(group_test)

    # DELETE
    def delete_group_test(self, teacher_id: str, group_test_id: str):
        group_test = self.dao_group_test.get_group_test_by_id(group_test_id)

        if not group_test:
            raise Exception(f"Group test {group_test_id} not found")
        if self.dao_group.check_owner(group_test.group_id, teacher_id) is False:
            raise Exception(f"Teacher {teacher_id} is not the owner of group {group_test.group_id}")

        self.dao_group_test.delete_group_test(group_test_id)
