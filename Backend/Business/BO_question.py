import os
import pickle

from fastapi import UploadFile

from Backend.Business import IMAGE_EXTENSIONS, AUDIO_EXTENSIONS, STATIC_PATH
from Backend.DataAccess.DAO_question import DAO_question
from Backend.DataAccess.DAO_question_bank import DAO_question_bank
from Backend.Model.DB_model import Question
from Backend.Model.request_model import Req_Question


class BO_question:
    def __init__(self):
        self._dao_question = None
        self._dao_question_bank = None

    @property
    def dao_question_bank(self) -> DAO_question_bank:
        if self._dao_question_bank is None:
            self._dao_question_bank = DAO_question_bank()
        return self._dao_question_bank

    @property
    def dao_question(self) -> DAO_question:
        if self._dao_question is None:
            self._dao_question = DAO_question()
        return self._dao_question

    # INSERT
    def insert_question(self, question_bank_id: str, data: Req_Question) -> str:
        return self.dao_question.insert_question(Question({
            'question_bank_id': question_bank_id,
            'content': data.content,
            'answer': pickle.dumps([{'content': a.content, 'is_correct': a.is_correct} for a in
                                    (data.answer if data.answer is not None else [])]),
            'difficulty': data.difficulty
        }))

    def insert_questions(self, teacher_id: str, question_bank_id: str, data: list[Req_Question]) -> list[str]:
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")
        if len(data) == 1:
            return self.insert_question(question_bank_id, data[0])
        return self.dao_question.insert_questions(question_bank_id, [Question({
            'content': q.content,
            'answer': pickle.dumps([{'content': a.content, 'is_correct': a.is_correct} for a in
                                    (q.answer if q.answer is not None else [])]),
            'difficulty': q.difficulty
        }) for q in data])

    def insert_attachment(self, teacher_id: str, question_id: str, attachment: list[UploadFile]):
        if self.dao_question.check_owner(teacher_id=teacher_id, question_id=question_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question {question_id}!")
        for file in attachment:
            _, extension = os.path.splitext(file.filename)
            if extension.lower() not in IMAGE_EXTENSIONS and AUDIO_EXTENSIONS:
                raise ValueError("Not supported extension: " + str(IMAGE_EXTENSIONS))

            relative_path = os.path.join("Teacher", teacher_id, "Question", teacher_id + extension)
            abs_path = os.path.join(STATIC_PATH, relative_path)

    # SELECT
    def get_questions_in_bank(self, teacher_id: str, question_bank_id: str, offset: int, length: int) -> list[Question]:
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")
        return self.dao_question.get_questions_in_bank(question_bank_id, offset=offset, length=length)

    def count_questions_in_bank(self, teacher_id, question_bank_id):
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")
        return self.dao_question.count_questions_in_bank(question_bank_id)

    # UPDATE
    def update_questions(self, teacher_id: str, question_bank_id: str, data: list[Req_Question]):
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")
        self.dao_question.update_questions(question_bank_id, [Question({
            'id': q.id,
            'content': q.content,
            'answer': pickle.dumps([{'content': a.content, 'is_correct': a.is_correct} for a in
                                    q.answer]) if q.answer is not None else None,
            'difficulty': q.difficulty
        }) for q in data])

    # DELETE
    def delete_questions(self, teacher_id: str, question_bank_id: str, question_ids: list[str]):
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")

        if len(question_ids) == 1:
            self.dao_question.delete_question(question_bank_id=question_bank_id, question_id=question_ids[0])
        else:
            self.dao_question.delete_questions(question_bank_id=question_bank_id, question_ids=question_ids)
