from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from Backend.Business.authenticate_BO import create_access_token
from Backend.Business.teacher_BO import teacher_BO
from Backend.Business.student_BO import student_BO
from Backend.Model.response_model import Res_Token
from Backend.Model.db_model import Teacher, Student

auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post("/token")
async def get_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], role: str) -> Res_Token:
    if role == "teacher":
        teacher_service = teacher_BO()
        teacher: Teacher = teacher_service.authenticate(form_data.username, form_data.password)
        if not teacher:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token = create_access_token({"id": teacher.id, "email": teacher.email, "role": role})

        return Res_Token(**{"access_token": token, "token_type": 'bearer'})

    if role == "student":
        student_service = student_BO()
        student: Student = student_service.authenticate(form_data.username, form_data.password)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token = create_access_token({"id": student.id, "email": student.email, "role": role})

        return Res_Token(**{"access_token": token, "token_type": 'bearer'})

    if role == "admin":
        pass

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Need role: ['teacher', 'student', 'admin']",
    )
