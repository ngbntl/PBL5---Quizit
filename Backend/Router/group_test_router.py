from fastapi import APIRouter, HTTPException, Depends, Body, Query
from typing import Annotated
from starlette import status

from Backend.Business.BO_group_test import BO_group_test
from Backend.Business.BO_student_test import BO_student_test
from Backend.Model.DB_model import Teacher, Student
from Backend.Business.BO_authenticate import get_current_user
from Backend.Model.request_model import Req_GroupTest, Req_StudentWork
from Backend.Model.response_model import Res_GroupTest, Res_StudentTest

teacher_group_test_router = APIRouter(prefix='/grouptest', tags=['grouptest'])
student_group_test_router = APIRouter(prefix='/grouptest', tags=['grouptest'])


### TEACHER ###
# INSERT
@teacher_group_test_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_GroupTest, Body()],
                            group_test_service: Annotated[BO_group_test, Depends()]):
    try:
        return group_test_service.insert_group_test(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# SELECT
@teacher_group_test_router.get('/', status_code=status.HTTP_200_OK)
@student_group_test_router.get('/', status_code=status.HTTP_200_OK)
async def get_group_test(_: Annotated[Teacher | Student, Depends(get_current_user)],
                         group_test_service: Annotated[BO_group_test, Depends()],
                         group_id: Annotated[str, Query(min_length=8, max_length=8)]):
    try:
        return [Res_GroupTest.from_DB_model(group_test) for group_test in
                group_test_service.get_group_test_in_group(group_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_test_router.get('/studentwork', status_code=status.HTTP_200_OK)
async def get_studentworks(teacher: Annotated[Teacher, Depends(get_current_user)],
                           group_test_service: Annotated[BO_group_test, Depends()],
                           group_test_id: Annotated[str, Query(min_length=8, max_length=8)],
                           student_id: Annotated[str, Query(min_length=8, max_length=8)] = None):
    try:
        if student_id is not None:
            return Res_StudentTest.from_DB_model(group_test_service.get_studentwork(group_test_id, student_id))

        return [Res_StudentTest.from_DB_model(student_test) for student_test in
                group_test_service.get_studentworks(group_test_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_test_router.get('/studentpoint', status_code=status.HTTP_200_OK, response_model=list[Res_StudentTest],
                               response_model_exclude_none=True)
async def get_studentpoint(teacher: Annotated[Teacher, Depends(get_current_user)],
                           group_test_service: Annotated[BO_group_test, Depends()],
                           group_test_id: Annotated[str, Query(min_length=8, max_length=8)]):
    try:
        return [Res_StudentTest.from_DB_model(student_test) for student_test in
                group_test_service.get_studentpoints_by_test(group_test_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# UPDATE
@teacher_group_test_router.put('/', status_code=status.HTTP_200_OK)
async def update_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            group_test_service: Annotated[BO_group_test, Depends()],
                            data: Annotated[Req_GroupTest, Body()]):
    try:
        group_test_service.update_group_test(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# DELETE
@teacher_group_test_router.delete('/teacher', status_code=status.HTTP_200_OK)
async def delete_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            group_test_id: Annotated[str, Query(min_length=8, max_length=8)],
                            group_test_service: Annotated[BO_group_test, Depends()]):
    try:
        group_test_service.delete_group_test(teacher.id, group_test_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


### STUDENT ###
@student_group_test_router.get('/studentwork/', status_code=status.HTTP_200_OK)
async def get_student_test(student: Annotated[Student, Depends(get_current_user)],
                           group_test_service: Annotated[BO_student_test, Depends()],
                           group_test_id: Annotated[str, Query(min_length=8, max_length=8)]):
    try:
        return Res_StudentTest.from_DB_model(
            group_test_service.get_student_test_by_group_test_id(student.id, group_test_id))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_test_router.post('/studentwork/submit', status_code=status.HTTP_200_OK)
async def update_student_work(student: Annotated[Student, Depends(get_current_user)],
                              data: Annotated[Req_StudentWork, Body()],
                              group_test_service: Annotated[BO_student_test, Depends()]) -> float:
    try:
        return group_test_service.submit(student.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
