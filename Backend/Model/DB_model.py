import json
from datetime import datetime


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


class Question:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.question_bank_id: str | None = data.get("question_bank_id")
        self.order_number: int | None = data.get("order_number")
        self.content: str | None = data.get("content")
        self.answer: bytes | None = data.get("answer")
        self.attachment: str | None = data.get("attachment")
        self.difficulty: int | None = data.get("difficulty")


class Test:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.collection_id: str | None = data.get("collection_id")
        self.name: str | None = data.get("name")
        self.reference_question_bank: str | None = data.get("reference_question_bank")
        self.created_timestamp: datetime | None = data.get("created_timestamp")


class GroupTest:
    def __init__(self, data: dict) -> None:
        self.id: str | None = data.get("id")
        self.group_id: str | None = data.get("group_id")
        self.test_id: str | None = data.get("test_id")
        self.start: datetime | None = data.get("start")
        self.end: datetime | None = data.get("end")
        self.created_timestamp: datetime | None = data.get("created_timestamp")


class IEncoder(json.JSONEncoder):
    def default(self, obj):
        return dict(obj)
