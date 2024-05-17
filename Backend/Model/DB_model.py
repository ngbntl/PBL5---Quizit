import pickle
from datetime import datetime

from Backend.Model.request_model import Req_Question
from Backend.Model.response_model import Res_Question, Res_StudentTest


class Admin:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.username: str | None = data.get("username")
        self.hash_pswd: str | None = data.get("hash_pswd")
        self.name: str | None = data.get("name")
        self.is_banned: bool | None = data.get("is_banned")


class Student:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.email: str | None = data.get("email")
        self.hash_pswd: str | None = data.get("hash_pswd")
        self.name: str | None = data.get("name")
        self.avatar_path: str | None = data.get("avatar_path")
        self.is_banned: bool | None = data.get("is_banned")
        self.created_timestamp: datetime | None = data.get("created_timestamp")
        self.is_verified: bool | None = data.get("is_verified")


class Teacher:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.email: str | None = data.get("email")
        self.hash_pswd: str | None = data.get("hash_pswd")
        self.name: str | None = data.get("name")
        self.avatar_path: str | None = data.get("avatar_path")
        self.is_banned: bool | None = data.get("is_banned")
        self.created_timestamp: datetime | None = data.get("created_timestamp")
        self.is_verified: bool | None = data.get("is_verified")


class Group:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.name: str | None = data.get("name")
        self.teacher_id: str | None = data.get("teacher_id")
        self.created_timestamp: datetime | None = data.get("created_timestamp")
        self.is_show: bool | None = data.get("is_show")


class GroupStudent:
    def __init__(self, data: dict) -> None:
        self.group_id: str | None = data.get("group_id")
        self.student_id: str | None = data.get("student_id")
        self.is_join: bool | None = data.get("is_join")
        self.request_timestamp: datetime | None = data.get("request_timestamp")
        self.is_show: bool | None = data.get("is_show")


class Collection:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.teacher_id: str | None = data.get("teacher_id")
        self.name: str | None = data.get("name")
        self.created_timestamp: datetime | None = data.get("created_timestamp")


class QuestionBank:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.collection_id: str | None = data.get("collection_id")
        self.name: str | None = data.get("name")
        self.created_timestamp: datetime | None = data.get("created_timestamp")


class Answer:
    def __init__(self, data: dict) -> None:
        self.content: str | None = data.get("content")
        self.is_correct: bool | None = data.get("is_correct")


class Question:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.question_bank_id: str | None = data.get("question_bank_id")
        self.order_number: int | None = data.get("order_number")
        self.content: str | None = data.get("content")
        self.answer: bytes | None = data.get("answer")
        self.attachment: bytes | None = data.get("attachment")
        self.difficulty: int | None = data.get("difficulty")

    @classmethod
    def construct_from_req(cls, req: Req_Question):
        question = cls(req.model_dump())
        question.answer = pickle.dumps([{'content': a.content, 'is_correct': a.is_correct} for a in
                                        (req.answer if isinstance(req.answer, list) else [])])
        return question

    def convert_to_res(self) -> Res_Question:
        return Res_Question(id=self.id, order_number=self.order_number, content=self.content,
                            answer=pickle.loads(self.answer),
                            attachment=pickle.loads(self.attachment) if self.attachment else None,
                            difficulty=self.difficulty)


class Test:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.collection_id: str | None = data.get("collection_id")
        self.name: str | None = data.get("name")
        self.created_timestamp: datetime | None = data.get("created_timestamp")


class NumberOfQuestion:
    def __init__(self, data: dict) -> None:
        self.test_id: str | None = data.get("test_id")
        self.question_bank_id: str | None = data.get("question_bank_id")
        self.number_of_question: int | None = data.get("number_of_question")


class TestStructure:
    def __init__(self, data: dict) -> None:
        self.test_id: str | None = data.get("test_id")
        self.question_bank_id: str | None = data.get("question_bank_id")
        self.number_of_question: bytes | None = data.get("number_of_question")


class GroupTest:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.group_id: str | None = data.get("group_id")
        self.test_id: str | None = data.get("test_id")
        self.name: str | None = data.get("name")
        self.start: datetime | None = data.get("start")
        self.end: datetime | None = data.get("end")
        self.duration: int | None = data.get("duration")
        self.shuffle: bool | None = data.get("shuffle")
        self.created_timestamp: datetime | None = data.get("created_timestamp")


class StudentTest:
    def __init__(self, data: dict) -> None:
        self.student_id: str | None = data.get("student_id")
        self.group_test_id: str | None = data.get("group_test_id")
        self.start: datetime | None = data.get("start")
        self.end: datetime | None = data.get("end")
        self.student_work: bytes | None = data.get("student_work")
        self.score: int | None = data.get("score")

    def convert_to_res(self) -> Res_StudentTest:
        return Res_StudentTest(student_id=self.student_id, group_test_id=self.group_test_id, start=self.start,
                               end=self.end, student_work=pickle.loads(self.student_work), score=self.score)


class StudentWork_Question:
    def __init__(self, data: dict) -> None:
        self.content: str | None = data.get("content")
        self.answer: list | None = data.get("answer")
        self.attachment: list[str] | None = data.get("attachment")
        self.student_answer: bytes | None = data.get("student_answer")


class StudentWork:
    def __init__(self, data: dict) -> None:
        self.student_work = data.get("student_work")
