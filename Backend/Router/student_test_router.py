from fastapi import APIRouter, HTTPException, Depends, Body
from starlette import status
from typing import Annotated

from Backend.Model.DB_model import Student
from Backend.Model.request_model import Req_StudentWork, Req_StudentTest
from Backend.Business.BO_student_test import BO_student_test
from Backend.Business.BO_authenticate import get_current_user
from Backend.Model.response_model import Res_StudentTest

student_test_router = APIRouter(prefix='/test', tags=['test'])


# SELECT
@student_test_router.get('/', status_code=status.HTTP_200_OK)
async def get_student_test(student: Annotated[Student, Depends(get_current_user)],
                           group_test_service: Annotated[BO_student_test, Depends()],
                           data: Annotated[Req_StudentTest, Body()]) -> Res_StudentTest:
    try:
        data.student_id = student.id
        return group_test_service.get_student_test(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_test_router.post('/submit', status_code=status.HTTP_200_OK)
async def update_student_work(student: Annotated[Student, Depends(get_current_user)],
                              data: Annotated[Req_StudentWork, Body()],
                              group_test_service: Annotated[BO_student_test, Depends()]) -> float:
    try:
        return 5.0
        # return group_test_service.submit(student.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
