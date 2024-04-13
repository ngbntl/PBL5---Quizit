import asyncio
import os

from fastapi import UploadFile

from Backend.Model.db_model import Student
from Backend.Model.request_model import Req_Student
from Backend.DataAccess.student_DA import student_DA
from Backend.Business import bcrypt_context, IMAGE_EXTENSIONS, save_file, STATIC_PATH


class student_BO:
    def __init__(self):
        self.student_DA = student_DA()

    # SELECT
    def authenticate(self, username: str, password: str) -> Student | None:
        student = Student(self.student_DA.get_student_by_email(email=username))
        if student:
            if bcrypt_context.verify(password, student.hash_pswd):
                return student
        return None

    def get_student_by_id(self, student_id: str) -> dict | None:
        return self.student_DA.get_student_by_id(student_id)

    # INSERT
    def sign_up(self, data: Req_Student) -> str:
        if data.email is None:
            raise ValueError("Email is required!")
        if data.password is None:
            raise ValueError("Password is required!")
        if data.name is None:
            raise ValueError("Name is required!")
        return self.student_DA.insert_student(data, bcrypt_context.hash(data.password))

    # UPDATE
    def update_student(self, student_id: str, data: Req_Student):
        if data.password is not None:
            self.update_password(student_id, data.password)
        if data.name is not None:
            self.update_name(student_id, data.name)

    def update_password(self, teacher_id: str, password: str) -> None:
        self.student_DA.update_password(teacher_id, bcrypt_context.hash(password))

    def update_name(self, teacher_id: str, name: str) -> None:
        self.student_DA.update_name(teacher_id, name)

    def update_is_banned(self, teacher_id: str, is_banned: bool) -> None:
        self.student_DA.update_is_banned(teacher_id, is_banned)

    def update_is_verified(self, teacher_id: str, is_verified: bool) -> None:
        self.student_DA.update_is_verified(teacher_id, is_verified)

    async def update_avatar(self, student_id: str, image: UploadFile) -> None:
        _, extension = os.path.splitext(image.filename)
        if extension.lower() not in IMAGE_EXTENSIONS:
            raise ValueError("Not supported extension: " + str(IMAGE_EXTENSIONS))
        relative_path = os.path.join("Student", student_id, "Avatar", student_id + extension)
        abs_path = os.path.join(STATIC_PATH, relative_path)
        await asyncio.gather(self.upload_avatar_path(student_id, relative_path), save_file(abs_path, image))
        return relative_path

    async def upload_avatar_path(self, student_id: str, avatar_path: str):
        self.student_DA.update_avatar_path(student_id, avatar_path)
