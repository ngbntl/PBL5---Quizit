from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Body, Query, UploadFile, File
from starlette import status
from Backend.Business.BO_authenticate import get_current_user
from Backend.Business.BO_question import BO_question
from Backend.Model.DB_model import Teacher
from Backend.Model.request_model import Req_Question
from Backend.Model.response_model import Res_Question, Res_NumberOfQuestion

question_router = APIRouter(prefix='/question', tags=['question'])


# INSERT
@question_router.post('/', status_code=status.HTTP_200_OK)
async def insert_questions(teacher: Annotated[Teacher, Depends(get_current_user)],
                           question_bank_id: Annotated[str, Query(min_length=8, max_length=8)],
                           data: Annotated[list[Req_Question], Body()],
                           question_service: Annotated[BO_question, Depends()]):
    try:
        return question_service.insert_questions(teacher_id=teacher.id, question_bank_id=question_bank_id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@question_router.post('/attachment', status_code=status.HTTP_200_OK)
async def insert_attachment(teacher: Annotated[Teacher, Depends(get_current_user)],
                            question_id: Annotated[str, Query(min_length=10, max_length=10)],
                            attachment: Annotated[list[UploadFile], File()],
                            question_service: Annotated[BO_question, Depends()]) -> list[str]:
    try:
        return await question_service.insert_attachment(teacher_id=teacher.id, question_id=question_id,
                                                        attachment=attachment)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# SELECT
@question_router.get('/', status_code=status.HTTP_200_OK, response_model_exclude_unset=True)
async def get_questions_in_bank(teacher: Annotated[Teacher, Depends(get_current_user)],
                                question_bank_id: Annotated[str, Query(min_length=8, max_length=8)],
                                question_service: Annotated[BO_question, Depends()],
                                offset: int = Query(default=1, ge=1),
                                length: int = Query(default=50, ge=0, le=100)) -> list[Res_Question]:
    try:
        return question_service.get_questions_in_bank(teacher_id=teacher.id, question_bank_id=question_bank_id,
                                                      offset=offset, length=length)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@question_router.get('/summary', status_code=status.HTTP_200_OK, response_model=list[Res_NumberOfQuestion])
async def question_summary(teacher: Annotated[Teacher, Depends(get_current_user)],
                           question_bank_id: Annotated[str, Query(min_length=8, max_length=8)],
                           question_service: Annotated[BO_question, Depends()]) -> int:
    try:
        return question_service.summary(teacher_id=teacher.id, question_bank_id=question_bank_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# UPDATE
@question_router.put('/', status_code=status.HTTP_200_OK)
async def update_questions(teacher: Annotated[Teacher, Depends(get_current_user)],
                           question_bank_id: Annotated[str, Query(min_length=8, max_length=8)],
                           data: Annotated[list[Req_Question], Body()],
                           question_service: Annotated[BO_question, Depends()]) -> None:
    try:
        question_service.update_questions(teacher_id=teacher.id, question_bank_id=question_bank_id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# DELETE
@question_router.delete('/', status_code=status.HTTP_200_OK)
async def delete_questions(teacher: Annotated[Teacher, Depends(get_current_user)],
                           question_bank_id: Annotated[str, Query(min_length=8, max_length=8)],
                           list_id: Annotated[list[str], Body(...)],
                           question_service: Annotated[BO_question, Depends()]) -> None:
    try:
        question_service.delete_questions(teacher_id=teacher.id, question_bank_id=question_bank_id,
                                          question_ids=list_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@question_router.delete('/attachment', status_code=status.HTTP_200_OK)
async def delete_attachment(teacher: Annotated[Teacher, Depends(get_current_user)],
                            attachment_path: Annotated[str, Body()],
                            question_service: Annotated[BO_question, Depends()]) -> None:
    try:
        question_service.delete_attachment(teacher_id=teacher.id, attachment_path=attachment_path)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
