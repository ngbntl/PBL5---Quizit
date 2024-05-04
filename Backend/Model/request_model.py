from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class Req_Admin(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    username: str = Field(None, max_length=255)
    password: str = Field(None, min_length=8, max_length=64)
    name: str = Field(None, max_length=100)
    is_banned: bool = False


class Req_Teacher(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    email: EmailStr = None
    password: str = Field(None, min_length=8, max_length=64)
    name: str = Field(None, max_length=100)
    is_banned: bool = False
    is_verified: bool = False


class Req_Student(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    email: EmailStr = None
    password: str = Field(None, min_length=8, max_length=64)
    name: str = Field(None, max_length=100)
    is_banned: bool = False
    is_verified: bool = False


class Req_Group(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)
    teacher_id: str = Field(None, min_length=8, max_length=8)
    is_show: bool = True


class Req_GroupStudent(BaseModel):
    group_id: str = Field(None, min_length=8, max_length=8)
    student_id: str = Field(None, min_length=8, max_length=8)
    is_join: bool = True
    is_show: bool = True


class Req_GroupTest(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    group_id: str = Field(None, min_length=8, max_length=8)
    test_id: str = Field(None, min_length=8, max_length=8)
    start: datetime = None
    end: datetime = None


class Req_Collection(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    teacher_id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)


class Req_QuestionBank(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    collection_id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)


class Req_Test(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    collection_id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)


class Req_Answer(BaseModel):
    content: str = Field(None, max_length=256)
    is_correct: bool = False


class Req_Question(BaseModel):
    id: str = Field(None, min_length=10, max_length=10)
    question_bank_id: str = Field(None, min_length=8, max_length=8)
    content: str = Field(None, max_length=512)
    answer: list[Req_Answer] = None
    difficulty: int = Field(None, ge=1, le=5)


class Req_NumberOfQuestion(BaseModel):
    difficulty: int = Field(ge=1, le=5)
    number_of_question: int = Field(ge=1)


class Req_TestStructure(BaseModel):
    test_id: str = Field(min_length=8, max_length=8)
    question_bank_id: str = Field(min_length=8, max_length=8)
    number_of_question: list[Req_NumberOfQuestion]


class Req_GroupTest(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    group_id: str = Field(None, min_length=8, max_length=8)
    test_id: str = Field(None, min_length=8, max_length=8)
    start: datetime = None
    end: datetime = None
    duration: int = Field(None, ge=1, le=180)
    shuffle: bool = False
