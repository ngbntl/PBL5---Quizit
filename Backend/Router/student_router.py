from fastapi import APIRouter, HTTPException, Depends, Body, File, UploadFile
from starlette import status
from typing import Annotated
from Backend.Model.db_model import Teacher
from Backend.Model.request_model import Req_Student
from Backend.Model.response_model import Res_Student
from Backend.Business.student_business import student_bussiness
from Backend.Business.authenticate_bussiness import get_current_user
from Backend.Router.group_router import student_group_router

student_router = APIRouter(prefix='/student', tags=['student'])
student_router.include_router(student_group_router)


@student_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[Req_Student, Body(...)],
                  student_service: Annotated[student_bussiness, Depends()]) -> str:
    """
    Sign up student
    :param data:
    :param student_service:
    :return:
    """
    try:
        return student_service.sign_up(data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@student_router.get('/', status_code=status.HTTP_200_OK, response_model=Res_Student, response_model_exclude_unset=True)
async def get_student(student: Annotated[Teacher, Depends(get_current_user)],
                      student_service: Annotated[student_bussiness, Depends()]):
    """
    Get student information
    :param student:
    :param student_service:
    :return:
    """
    try:
        return Res_Student(**student_service.get_student_by_id(student.id))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@student_router.patch('/update', status_code=status.HTTP_200_OK)
async def update(data: Annotated[Req_Student, Body(...)],
                 student: Annotated[Teacher, Depends(get_current_user)],
                 student_service: Annotated[student_bussiness, Depends()]):
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
async def update_avatar(image: Annotated[UploadFile, File(description="Upload avatar")],
                        student: Annotated[Teacher, Depends(get_current_user)],
                        student_service: Annotated[student_bussiness, Depends()]):
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
