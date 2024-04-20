from fastapi import APIRouter, HTTPException, Depends, Body, Query, Path
from starlette import status
from typing import Annotated, Union

from Backend.Model.request_model import Req_Group, Req_GroupStudent
from Backend.Model.response_model import Res_Group, Res_Student
from Backend.Model.DB_model import Teacher, Student
from Backend.Business.BO_group import BO_group
from Backend.Business.BO_group_student import BO_group_student
from Backend.Business.BO_authenticate import get_current_user

student_group_router = APIRouter(prefix='/group', tags=['group', 'student'])
teacher_group_router = APIRouter(prefix='/group', tags=['group', 'teacher'])


### TEACHER ###
@teacher_group_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_group(teacher: Annotated[Teacher, Depends(get_current_user)],
                       data: Annotated[Req_Group, Body()],
                       group_service: Annotated[BO_group, Depends()]):
    try:
        return group_service.insert_group(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# @teacher_group_router.get('/', response_model=list[Res_Group], status_code=status.HTTP_200_OK,
#                           response_model_exclude_unset=True)
# async def get_groups(teacher: Annotated[Teacher, Depends(get_current_user)],
#                      group_service: Annotated[group_business, Depends()],
#                      is_show: Annotated[bool, Query()] = True):
#     try:
#
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@teacher_group_router.get('/', response_model=Union[Res_Group, list[Res_Group]], status_code=status.HTTP_200_OK,
                          response_model_exclude_unset=True)
async def get_group(teacher: Annotated[Teacher, Depends(get_current_user)],
                    group_service: Annotated[BO_group, Depends()],
                    is_show: Annotated[bool, Query()] = True,
                    group_id: Annotated[Union[str, None], Query(min_length=8, max_length=8)] = None):
    try:
        if group_id is not None:
            group = group_service.get_group_by_id(group_id, teacher.id)
            return Res_Group(id=group.id, name=group.name, created_timestamp=group.created_timestamp, is_show=group.is_show)
        else:
            return [Res_Group(id=group.id, name=group.name, created_timestamp=group.created_timestamp, is_show=group.is_show) for group in
                    group_service.get_groups_by_teacher(teacher.id, is_show)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.patch('/update', status_code=status.HTTP_204_NO_CONTENT)
async def update_visibility(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_Group, Body()],
                            group_service: Annotated[BO_group, Depends()]):
    try:
        group_service.update_group(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.post('/student', status_code=status.HTTP_201_CREATED)
async def insert_students(teacher: Annotated[Teacher, Depends(get_current_user)],
                          list_id: Annotated[list[Annotated[str, Body(min_length=8, max_length=8)]], Body()],
                          group_id: Annotated[str, Query(min_length=8, max_length=8)],
                          group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.insert_students(teacher_id=teacher.id, group_id=group_id, list_id=list_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.get('/student', response_model=list[Res_Student], status_code=status.HTTP_200_OK)
async def get_students_in_group(_: Annotated[Teacher, Depends(get_current_user)],
                                group_student_service: Annotated[BO_group_student, Depends()],
                                data: Annotated[Req_GroupStudent, Body()]):
    try:
        return [Res_Student(**student.__dict__) for student in
                group_student_service.get_students_by_group(data.group_id, data.is_join)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.delete('/student', status_code=status.HTTP_204_NO_CONTENT)
async def delete_students(teacher: Annotated[Teacher, Depends(get_current_user)],
                          group_id: Annotated[str, Query(min_length=8, max_length=8)],
                          list_id: Annotated[list[Annotated[str, Body(min_length=8, max_length=8)]], Body()],
                          group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.delete_students(teacher.id, group_id, list_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# @teacher_group_router.patch('/request', status_code=status.HTTP_204_NO_CONTENT)
# async def update_join_requests(teacher: Annotated[Teacher, Depends(get_current_user)],
#                                group_id: Annotated[str, Query(min_length=8, max_length=8)],
#                                list_id: Annotated[list[Annotated[str, Body(min_length=8, max_length=8)]], Body()],
#                                group_student_service: Annotated[BO_group_student, Depends()]):
#     try:
#         group_student_service.update_join_requests(teacher.id, group_id, list_id)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


### STUDENT ###
@student_group_router.get('/', status_code=status.HTTP_200_OK)
async def get_groups(student: Annotated[Student, Depends(get_current_user)],
                     group_student_service: Annotated[BO_group_student, Depends()],
                     join: Annotated[bool, Query()] = True,
                     just_id: Annotated[bool, Query()] = True):
    try:
        if just_id:
            return group_student_service.get_group_id_by_student(student.id, join)
        else:
            return [Res_Group(**group.__dict__) for group in group_student_service.get_groups_by_student(student_id=student.id, is_join=join)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.post('/', status_code=status.HTTP_201_CREATED)
async def request_join_group(student: Annotated[Student, Depends(get_current_user)],
                             group_id: Annotated[str, Query(min_length=8, max_length=8)],
                             group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.request_join(group_id=group_id, student_id=student.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_student_group(student: Annotated[Student, Depends(get_current_user)],
                               data: Annotated[Req_GroupStudent, Body()],
                               group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.update_student_group(student.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.delete('/{group_id}', status_code=status.HTTP_204_NO_CONTENT)
async def leave_group(student: Annotated[Student, Depends(get_current_user)],
                      group_id: Annotated[str, Path(min_length=8, max_length=8)],
                      group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.leave_group(student.id, group_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
