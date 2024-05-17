from fastapi import APIRouter, HTTPException, Depends, Body, Query
from typing import Annotated

from starlette import status

from Backend.Business.BO_test import BO_test
from Backend.Model.DB_model import Teacher
from Backend.Business.BO_authenticate import get_current_user
from Backend.Model.request_model import Req_Test

test_router = APIRouter(prefix='/test', tags=['test'])

# SELECT
@test_router.get('/', status_code=status.HTTP_200_OK)
async def get_tests(teacher: Annotated[Teacher, Depends(get_current_user)],
                    collection_id: Annotated[str, Query(min_length=8, max_length=8)],
                    test_service: Annotated[BO_test, Depends()]):
    try:
        return test_service.get_test_by_collection(collection_id, teacher.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# INSERT
@test_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                      data: Annotated[Req_Test, Body()],
                      test_service: Annotated[BO_test, Depends()]) -> str:
    try:
        return test_service.insert_test(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
