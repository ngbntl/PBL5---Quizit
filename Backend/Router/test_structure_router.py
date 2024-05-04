from fastapi import APIRouter, HTTPException, Depends, Body, Query
from typing import Annotated
from starlette import status

from Backend.Business.BO_test_structure import BO_test_structure
from Backend.Model.DB_model import Teacher
from Backend.Business.BO_authenticate import get_current_user
from Backend.Model.request_model import Req_TestStructure
from Backend.Model.response_model import Res_TestStructure

test_structure_router = APIRouter(prefix='/structure', tags=['test'])


# INSERT
@test_structure_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_structure(teacher: Annotated[Teacher, Depends(get_current_user)],
                           data: Annotated[Req_TestStructure, Body()],
                           test_structure_service: Annotated[BO_test_structure, Depends()]):
    try:
        test_structure_service.insert_structure(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# SELECT
@test_structure_router.get('/')
async def get_structure(teacher: Annotated[Teacher, Depends(get_current_user)],
                        test_id: Annotated[str, Query()],
                        test_structure_service: Annotated[BO_test_structure, Depends()]) -> list[Res_TestStructure]:
    try:
        return test_structure_service.get_structure(test_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# UPDATE
async def update_structure(teacher: Annotated[Teacher, Depends(get_current_user)],
                           data: Annotated[Req_TestStructure, Body()],
                           test_structure_service: Annotated[BO_test_structure, Depends()]):
    try:
        test_structure_service.update_structure(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
