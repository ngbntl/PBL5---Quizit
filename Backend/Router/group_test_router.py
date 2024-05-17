from fastapi import APIRouter, HTTPException, Depends, Body, Query
from typing import Annotated
from starlette import status

from Backend.Business.BO_group_test import BO_group_test
from Backend.Model.DB_model import Teacher, Student
from Backend.Business.BO_authenticate import get_current_user
from Backend.Model.request_model import Req_GroupTest
from Backend.Model.response_model import Res_GroupTest

group_test_router = APIRouter(prefix='/grouptest', tags=['grouptest'])


### TEACHER ###
# INSERT
@group_test_router.post('/teacher', status_code=status.HTTP_201_CREATED)
async def insert_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_GroupTest, Body()],
                            group_test_service: Annotated[BO_group_test, Depends()]) -> str:
    try:
        return group_test_service.insert_group_test(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# SELECT
@group_test_router.get('/', status_code=status.HTTP_200_OK)
async def get_group_test(_: Annotated[Teacher | Student, Depends(get_current_user)],
                         group_test_service: Annotated[BO_group_test, Depends()],
                         group_id: Annotated[str, Query(min_length=8, max_length=8)]) -> list[Res_GroupTest]:
    try:
        return [Res_GroupTest(**group_test.__dict__) for group_test in
                group_test_service.get_group_test_in_group(group_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# UPDATE
@group_test_router.put('/teacher', status_code=status.HTTP_200_OK)
async def update_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            group_test_service: Annotated[BO_group_test, Depends()],
                            data: Annotated[Req_GroupTest, Body()]):
    try:
        group_test_service.update_group_test(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# DELETE
@group_test_router.delete('/teacher', status_code=status.HTTP_200_OK)
async def delete_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            group_test_id: Annotated[str, Query(min_length=8, max_length=8)],
                            group_test_service: Annotated[BO_group_test, Depends()]):
    try:
        group_test_service.delete_group_test(teacher.id, group_test_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
