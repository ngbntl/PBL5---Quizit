from fastapi import APIRouter, HTTPException, Depends, Body, Query
from starlette import status
from typing import Annotated

from Backend.Business.question_bank_BO import question_bank_BO
from Backend.Model.request_model import Req_QuestionBank
from Backend.Model.db_model import Teacher
from Backend.Business.authenticate_BO import get_current_user
from Backend.Model.response_model import Res_QuestionBank

question_bank_router = APIRouter(prefix='/question_bank', tags=['collection', 'teacher', 'question_bank'])

# INSERT
@question_bank_router.post('/', status_code=status.HTTP_200_OK)
async def insert_question_bank(teacher: Annotated[Teacher, Depends(get_current_user)],
                               data: Annotated[Req_QuestionBank, Body()],
                               question_bank_service: Annotated[question_bank_BO, Depends()]) -> str:
    try:
        return question_bank_service.insert_question_bank(teacher_id=teacher.id, collection_id=data.collection_id,
                                                          name=data.name)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# SELECT
@question_bank_router.get('/', response_model=list[Res_QuestionBank], status_code=status.HTTP_200_OK, response_model_exclude_unset=True)
async def get_question_banks_by_collection(teacher: Annotated[Teacher, Depends(get_current_user)],
                                           collection_id: Annotated[str, Query(min_length=8, max_length=8)],
                                           question_bank_service: Annotated[question_bank_BO, Depends()]):
    try:
        return [Res_QuestionBank(id=question_bank.get('id'), name=question_bank.get('name'), created_timestamp=question_bank.get('created_timestamp')) for question_bank in
                question_bank_service.get_question_banks_by_collection(teacher_id=teacher.id,
                                                                       collection_id=collection_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# UPDATE
@question_bank_router.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_question_bank(teacher: Annotated[Teacher, Depends(get_current_user)],
                               data: Annotated[Req_QuestionBank, Body()],
                               question_bank_service: Annotated[question_bank_BO, Depends()]) -> None:
    try:
        question_bank_service.update_question_bank(teacher_id=teacher.id, question_bank_id=data.id, name=data.name)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
