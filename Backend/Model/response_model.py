from datetime import datetime

from pydantic import BaseModel


class Res_Token(BaseModel):
    access_token: str
    token_type: str


class Res_Student(BaseModel):
    id: str
    email: str
    name: str | None = None
    avatar_path: str | None = None
    is_banned: bool | None = None
    created_timestamp: datetime | None = None
    is_verified: bool | None = None


class Res_Teacher(BaseModel):
    id: str
    email: str
    name: str | None = None
    avatar_path: str | None = None
    is_banned: bool | None = None
    created_timestamp: datetime | None = None
    is_verified: bool | None = None


class Res_Group(BaseModel):
    id: str
    name: str | None = None
    teacher_id: str | None = None
    created_timestamp: datetime | None = None
    is_show: bool | None = None


class Res_GroupStudent(BaseModel):
    group_id: str
    student_id: str
    is_join: bool | None = None
    request_timestamp: datetime | None = None
    is_show: bool | None = None


class Res_Collection(BaseModel):
    id: str
    teacher_id: str
    name: str | None = None
    created_timestamp: datetime | None


class Res_QuestionBank(BaseModel):
    id: str
    collection_id: str | None = None
    name: str | None = None
    created_timestamp: datetime | None = None


class Test(BaseModel):
    id: str
    collection_id: str
    name: str | None = None
    created_timestamp: datetime | None = None


class Res_GroupTest(BaseModel):
    id: str
    group_id: str
    test_id: str | None = None
    start: datetime | None = None
    end: datetime | None = None
    created_timestamp: datetime | None = None


class Res_Answer(BaseModel):
    id: str | None = None
    content: str | None = None
    is_correct: bool | None = None


class Res_Question(BaseModel):
    id: str | None = None
    question_bank_id: str | None = None
    order_number: int | None = None
    content: str | None = None
    answer: list[Res_Answer] | None = None
    attachment: list[str] | None = None
    difficulty: int | None = None
