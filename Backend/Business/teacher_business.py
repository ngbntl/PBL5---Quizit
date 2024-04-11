import asyncio
import os.path

from fastapi import UploadFile

from Backend.Model.db_model import Teacher
from Backend.Model.request_model import Req_Teacher
from Backend.DataAccess.teacher_DA import teacher_DA
from Backend.Business import bcrypt_context, STATIC_PATH, save_file, IMAGE_EXTENSIONS


class teacher_bussiness:
    def __init__(self):
        self.teacher_DA = teacher_DA()

    # SELECT
    def authenticate(self, username: str, password: str) -> Teacher | None:
        teacher = Teacher(self.teacher_DA.get_teacher_by_email(email=username))
        if teacher:
            if bcrypt_context.verify(password, teacher.hash_pswd):
                return teacher
        return None

    def get_teacher_by_id(self, teacher_id: str) -> dict | None:
        return self.teacher_DA.get_teacher_by_id(teacher_id)

    # INSERT
    def sign_up(self, data: Req_Teacher) -> str:
        if data.email is None:
            raise ValueError("Email is required!")
        if data.password is None:
            raise ValueError("Password is required!")
        if data.name is None:
            raise ValueError("Name is required!")
        return self.teacher_DA.insert_teacher(email=data.email, hash_pswd=bcrypt_context.hash(data.password), name=data.name)

    # UPDATE
    def update_teacher(self, teacher_id: str, data: Req_Teacher) -> None:
        if data.password is not None:
            self.update_password(teacher_id, data.password)
        if data.name is not None:
            self.update_name(teacher_id, data.name)

    def update_password(self, teacher_id: str, password: str) -> None:
        self.teacher_DA.update_password(teacher_id, bcrypt_context.hash(password))

    def update_name(self, teacher_id: str, name: str) -> None:
        self.teacher_DA.update_name(teacher_id, name)

    def update_is_banned(self, teacher_id: str, is_banned: bool) -> None:
        self.teacher_DA.update_is_banned(teacher_id, is_banned)

    def update_is_verified(self, teacher_id: str, is_verified: bool) -> None:
        self.teacher_DA.update_is_verified(teacher_id, is_verified)

    async def update_avatar(self, teacher_id: str, image: UploadFile) -> None:
        _, extension = os.path.splitext(image.filename)
        if extension.lower() not in IMAGE_EXTENSIONS:
            raise ValueError("Not supported extension: " + str(IMAGE_EXTENSIONS))
        relative_path = os.path.join("Teacher", teacher_id, "Avatar", teacher_id + extension)
        abs_path = os.path.join(STATIC_PATH, relative_path)
        await asyncio.gather(self.upload_avatar_path(teacher_id, relative_path), save_file(abs_path, image))
        return relative_path

    async def upload_avatar_path(self, teacher_id: str, avatar_path: str):
        self.teacher_DA.update_avatar_path(teacher_id, avatar_path)

