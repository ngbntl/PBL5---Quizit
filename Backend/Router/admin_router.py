from fastapi import APIRouter, HTTPException, Depends, Body, File, UploadFile
from starlette import status
from typing import Annotated
from Backend.Model.DB_model import Student
from Backend.Model.request_model import Req_Admin
from Backend.Model.response_model import Res_Student
from Backend.Business.BO_student import BO_student
from Backend.Business.BO_authenticate import get_current_user
from Backend.Router.group_router import student_group_router

admin_router = APIRouter(prefix='/admin', tags=['admin'])


@admin_router.post('/', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[Req_Admin, Body()],
                  student_service: Annotated[BO_student, Depends()]) -> str:
    try:
        return student_service.sign_up(data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@admin_router.get('/', status_code=status.HTTP_200_OK, response_model=Res_Student, response_model_exclude_unset=True)
async def get_student(student: Annotated[Student, Depends(get_current_user)],
                      student_service: Annotated[BO_student, Depends()]):
    """
    Get student information
    :param student:
    :param student_service:
    :return:
    """
    try:
        return Res_Student(**student_service.get_student_by_id(student.id).__dict__)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@student_router.patch('/information', status_code=status.HTTP_200_OK)
async def update(student: Annotated[Student, Depends(get_current_user)],
                 data: Annotated[Req_Student, Body()],
                 student_service: Annotated[BO_student, Depends()]):
    """
    Update student information
    :param data:
    :param student:
    :param student_service:
    :return:
    """
    try:
        student_service.update_student(student_id=student.id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@student_router.put('/avatar', status_code=status.HTTP_201_CREATED)
async def update_avatar(student: Annotated[Student, Depends(get_current_user)],
                        image: Annotated[UploadFile, File(description="Upload avatar")],
                        student_service: Annotated[BO_student, Depends()]):
    """
    Update student avatar
    :param image:
    :param student:
    :param student_service:
    :return:
    """
    try:
        return await student_service.update_avatar(student_id=student.id, image=image)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
