import pickle
from datetime import datetime


class Admin:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.username: str | None = data.get("username")
        self.hash_pswd: str | None = data.get("hash_pswd")
        self.name: str | None = data.get("name")
        self.is_banned: bool | None = data.get("is_banned")

    def jsonify(self):
        return self.__dict__


class Student:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.email: str | None = data.get("email")
        self.hash_pswd: str | None = data.get("hash_pswd")
        self.name: str | None = data.get("name")
        self.avatar_path: str | None = data.get("avatar_path")
        self.is_banned: bool | None = data.get("is_banned")
        self.created_timestamp: datetime | None = data.get("created_timestamp")
        self.is_verified: bool | None = data.get("is_verified")

    def jsonify(self):
        return self.__dict__


class Teacher:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.email: str | None = data.get("email")
        self.hash_pswd: str | None = data.get("hash_pswd")
        self.name: str | None = data.get("name")
        self.avatar_path: str | None = data.get("avatar_path")
        self.is_banned: bool | None = data.get("is_banned")
        self.created_timestamp: datetime | None = data.get("created_timestamp")
        self.is_verified: bool | None = data.get("is_verified")

    def jsonify(self):
        return self.__dict__


class Group:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.name: str | None = data.get("name")
        self.teacher_id: str | None = data.get("teacher_id")
        self.created_timestamp: datetime | None = data.get("created_timestamp")
        self.is_show: bool | None = data.get("is_show")

    def jsonify(self):
        return self.__dict__


class GroupStudent:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.group_id: str | None = data.get("group_id")
        self.student_id: str | None = data.get("student_id")
        self.is_join: bool | None = data.get("is_join")
        self.request_timestamp: datetime | None = data.get("request_timestamp")
        self.is_show: bool | None = data.get("is_show")

    def jsonify(self):
        return self.__dict__


class Collection:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.teacher_id: str | None = data.get("teacher_id")
        self.name: str | None = data.get("name")
        self.created_timestamp: datetime | None = data.get("created_timestamp")

    def jsonify(self):
        return self.__dict__


class QuestionBank:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.collection_id: str | None = data.get("collection_id")
        self.name: str | None = data.get("name")
        self.created_timestamp: datetime | None = data.get("created_timestamp")

    def jsonify(self):
        return self.__dict__


class Answer:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.text: list[str] | None = data.get("text")
        self.correct: set[int] | None = data.get("correct")

    def jsonify(self):
        return self.__dict__


class Question:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.question_bank_id: str | None = data.get("question_bank_id")
        self.order_number: int | None = data.get("order_number")
        self.content: str | None = data.get("content")
        self.answer: Answer | bytes | None = data.get("answer")
        self.attachment: list[str] | bytes | None = data.get("attachment")
        self.difficulty: int | None = data.get("difficulty")

        if isinstance(self.answer, bytes):
            self.answer = pickle.loads(self.answer)
        if isinstance(self.attachment, bytes):
            self.attachment = pickle.loads(self.attachment) if self.attachment else None

    def jsonify(self):
        return self.__dict__


class NumberOfQuestion:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.difficulty: int | None = data.get("difficulty")
        self.number_of_question: int | None = data.get("number_of_question")

    def jsonify(self):
        return self.__dict__


class Test:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.collection_id: str | None = data.get("collection_id")
        self.name: str | None = data.get("name")
        self.created_timestamp: datetime | None = data.get("created_timestamp")
        self.structure: list[TestStructure] | None = data.get("structure")

    def jsonify(self):
        return self.__dict__


class TestStructure:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.test_id: str | None = data.get("test_id")
        self.question_bank_id: str | None = data.get("question_bank_id")
        self.number_of_question: list[NumberOfQuestion] | bytes | None = data.get("number_of_question")

        if isinstance(self.number_of_question, bytes):
            self.number_of_question = pickle.loads(self.number_of_question)

    def jsonify(self):
        return self.__dict__


class GroupTest:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.id: str | None = data.get("id")
        self.group_id: str | None = data.get("group_id")
        self.test_id: str | None = data.get("test_id")
        self.name: str | None = data.get("name")
        self.start: datetime | None = data.get("start")
        self.end: datetime | None = data.get("end")
        self.duration: int | None = data.get("duration")
        self.shuffle: bool | None = data.get("shuffle")
        self.created_timestamp: datetime | None = data.get("created_timestamp")

    def jsonify(self):
        return self.__dict__


class StudentWork_Question:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.content: str | None = data.get("content")
        self.answer: Answer | None = data.get("answer")
        self.attachment: list[str] | None = data.get("attachment")
        self.student_answer: list[int] | bytes | None = data.get("student_answer")

        if isinstance(self.student_answer, bytes):
            self.student_answer = pickle.loads(self.student_answer)

    def jsonify(self):
        return self.__dict__


class StudentTest:
    def __init__(self, json: dict = None, **kwargs):
        data = {**json, **kwargs} if json else kwargs
        self.student_id: str | None = data.get("student_id")
        self.group_test_id: str | None = data.get("group_test_id")
        self.start: datetime | None = data.get("start")
        self.end: datetime | None = data.get("end")
        self.student_work: list[StudentWork_Question] | bytes | None = data.get("student_work")
        self.score: int | None = data.get("score")

        if isinstance(self.student_work, bytes):
            self.student_work = pickle.loads(self.student_work)

    def jsonify(self):
        return self.__dict__
