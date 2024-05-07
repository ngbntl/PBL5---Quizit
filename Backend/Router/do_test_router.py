from fastapi import APIRouter, HTTPException, Depends, Body, Query, Path
from starlette import status
from typing import Annotated, Union

from Backend.Model.request_model import Req_Group, Req_GroupStudent
from Backend.Model.response_model import Res_Group, Res_Student
from Backend.Model.DB_model import Teacher, Student
from Backend.Business.BO_group import BO_group
from Backend.Business.BO_group_student import BO_group_student
from Backend.Business.BO_authenticate import get_current_user

do_test_router = APIRouter(prefix='student_test')

@do_test_router.get('/')
