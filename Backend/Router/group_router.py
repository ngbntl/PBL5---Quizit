from fastapi import APIRouter, HTTPException, Depends, Body, Query, Path
from starlette import status
from typing import Annotated

from Backend.Model.request_model import Req_Group, Req_GroupStudent
from Backend.Model.response_model import Res_Group, Res_Student
from Backend.Model.db_model import Teacher, Student
from Backend.Business.group_business import group_business
from Backend.Business.group_student_business import group_student_business
from Backend.Business.authenticate_bussiness import get_current_user

student_group_router = APIRouter(prefix='/group', tags=['group', 'student'])
teacher_group_router = APIRouter(prefix='/group', tags=['group', 'teacher'])


### TEACHER ###
@teacher_group_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_group(teacher: Annotated[Teacher, Depends(get_current_user)],
                       data: Annotated[Req_Group, Body()],
                       group_service: Annotated[group_business, Depends()]):
    try:
        return group_service.insert_group(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.get('/', response_model=list[Res_Group], status_code=status.HTTP_200_OK,
                          response_model_exclude_unset=True)
async def get_groups(teacher: Annotated[Teacher, Depends(get_current_user)],
                     group_service: Annotated[group_business, Depends()],
                     is_show: Annotated[bool, Query()] = True):
    try:
        return [Res_Group(id=row.get('id'), name=row.get('name'), created_timestamp=row.get('created_timestamp'),
                          is_show=row.get('is_show')) for row in
                group_service.get_groups_by_teacher(teacher.id, is_show)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@teacher_group_router.get('/{group_id}', response_model=Res_Group, status_code=status.HTTP_200_OK, response_model_exclude_unset=True)
async def get_group_by_id(teacher: Annotated[Teacher, Depends(get_current_user)],
                          group_id: Annotated[str, Path(min_length=8, max_length=8)],
                          group_service: Annotated[group_business, Depends()]):
    try:
        group = group_service.get_group_by_id(group_id, teacher.id)
        return Res_Group(id=group.get('id'), name=group.get('name'), created_timestamp=group.get('created_timestamp'),
                         is_show=group.get('is_show'))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_visibility(teacher: Annotated[Teacher, Depends(get_current_user)],
                            group_id: Annotated[str, Body(min_length=8, max_length=8)],
                            visibility: Annotated[bool, Body(default=True)],
                            group_service: Annotated[group_business, Depends()]):
    try:
        group_service.update_visibility(teacher.id, group_id, visibility)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.post('/student', status_code=status.HTTP_201_CREATED)
async def insert_student(teacher: Annotated[Teacher, Depends(get_current_user)],
                         data: Annotated[Req_GroupStudent, Body()],
                         group_student_service: Annotated[group_student_business, Depends()]):
    try:
        group_student_service.insert_student(data.group_id, data.student_id, teacher.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.get('/student', response_model=list[Res_Student], status_code=status.HTTP_200_OK)
async def get_students_in_group(_: Annotated[Teacher, Depends(get_current_user)],
                                group_student_service: Annotated[group_student_business, Depends()],
                                group_id: Annotated[str, Query(min_length=8, max_length=8)],
                                join: Annotated[bool, Query()] = True) -> list[str]:
    try:
        return [Res_Student(**student) for student in group_student_service.get_students_by_group(group_id, join)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.delete('/student', status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(teacher: Annotated[Teacher, Depends(get_current_user)],
                         group_id: Annotated[str, Query(min_length=8, max_length=8)],
                         student_id: Annotated[str, Query(min_length=8, max_length=8)],
                         group_student_service: Annotated[group_student_business, Depends()]):
    try:
        group_student_service.delete_student(teacher.id, group_id, student_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.patch('/request', status_code=status.HTTP_204_NO_CONTENT)
async def update_request(teacher: Annotated[Teacher, Depends(get_current_user)],
                         group_id: Annotated[str, Query(min_length=8, max_length=8)],
                         student_id: Annotated[str, Query(min_length=8, max_length=8)],
                         accept: Annotated[bool, Query()],
                         group_student_service: Annotated[group_student_business, Depends()]):
    try:
        group_student_service.update_join_request(teacher.id, group_id, student_id, accept)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


### STUDENT ###
@student_group_router.get('/', status_code=status.HTTP_200_OK)
async def get_groups(student: Annotated[Student, Depends(get_current_user)],
                     group_student_service: Annotated[group_student_business, Depends()],
                     join: Annotated[bool, Query()] = True,
                     just_id: Annotated[bool, Query()] = True):
    try:
        if just_id:
            return group_student_service.get_group_id_by_student(student.id, join)
        else:
            return [Res_Group(**group) for group in group_student_service.get_groups_by_student(student.id, join)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.post('/', status_code=status.HTTP_201_CREATED)
async def join_group(student: Annotated[Student, Depends(get_current_user)],
                     group_id: Annotated[str, Query(min_length=8, max_length=8)],
                     group_student_service: Annotated[group_student_business, Depends()]):
    try:
        group_student_service.insert_student(group_id, student.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_visibility(student: Annotated[Student, Depends(get_current_user)],
                            group_id: Annotated[str, Query(min_length=8, max_length=8)],
                            group_student_service: Annotated[group_student_business, Depends()],
                            visibility: Annotated[bool, Query()] = False):
    try:
        group_student_service.update_visibility(group_id, student.id, visibility)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
