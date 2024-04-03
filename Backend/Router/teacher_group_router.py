from fastapi import APIRouter, HTTPException, Depends, Body
from Model.request_model import Req_Group

from starlette import status
from typing import Annotated
from Model.db_model import Teacher
from Business.collection_business import collection_business
from Business.authenticate_bussiness import get_current_user

teacher_group_router = APIRouter(prefix='/group', tags=['group', 'teacher'])


@teacher_group_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_group(data: Annotated[Req_Group, Body(...)], group_serviced: Annotated[], teacher: Annotated[Teacher, Depends(get_current_user)]):
    return collection_business().insert_group(data, teacher.id)