from fastapi import APIRouter, HTTPException, Depends, Body, File, UploadFile
from starlette import status
from typing import Annotated

from Backend.Model.DB_model import Teacher
from Backend.Model.request_model import Req_Teacher
from Backend.Model.response_model import Res_Teacher
from Backend.Business.BO_authenticate import get_current_user
from Backend.Business.BO_teacher import BO_teacher
from Backend.Router.collection_router import collection_router
from Backend.Router.group_router import teacher_group_router

teacher_router = APIRouter(prefix='/teacher', tags=['teacher'])
teacher_router.include_router(collection_router)
teacher_router.include_router(teacher_group_router)


@teacher_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[Req_Teacher, Body()],
                  teacher_service: Annotated[BO_teacher, Depends()]):
    """
    Sign up teacher
    :param data:
    :param teacher_service:
    :return:
    """
    try:
        return teacher_service.sign_up(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@teacher_router.get('/', status_code=status.HTTP_200_OK, response_model=Res_Teacher, response_model_exclude_unset=True)
async def get_teacher(teacher: Annotated[Teacher, Depends(get_current_user)],
                      teacher_service: Annotated[BO_teacher, Depends()]):
    """
    Get teacher information
    :param teacher:
    :param teacher_service:
    :return:
    """
    try:
        return Res_Teacher(**teacher_service.get_teacher_by_id(teacher.id).__dict__)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@teacher_router.patch('/information', status_code=status.HTTP_200_OK)
async def update(data: Annotated[Req_Teacher, Body(...)],
                 teacher: Annotated[Teacher, Depends(get_current_user)],
                 teacher_service: Annotated[BO_teacher, Depends()]):
    """
    Update teacher information
    :param data:
    :param teacher:
    :param teacher_service:
    :return:
    """
    try:
        teacher_service.update_teacher(teacher_id=teacher.id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@teacher_router.put('/avatar', status_code=status.HTTP_201_CREATED)
async def update_avatar(image: Annotated[UploadFile, File(description="Upload avatar")],
                        teacher: Annotated[Teacher, Depends(get_current_user)],
                        teacher_service: Annotated[BO_teacher, Depends()]):
    """
    Update teacher avatar
    :param image:
    :param teacher:
    :param teacher_service:
    :return:
    """
    try:
        return await teacher_service.update_avatar(teacher_id=teacher.id, image=image)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
