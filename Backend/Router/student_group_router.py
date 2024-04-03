from fastapi import APIRouter, HTTPException, Depends, Body
from Model.request_model import Req_Collection
from Model.response_model import Res_Collection
from starlette import status
from typing import Annotated
from Model.db_model import Teacher
from Business.collection_business import collection_business
from Business.authenticate_bussiness import get_current_user

student_group_router = APIRouter(prefix='/group', tags=['group', 'student'])


