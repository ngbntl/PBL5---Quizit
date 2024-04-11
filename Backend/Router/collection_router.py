from fastapi import APIRouter, HTTPException, Depends, Body, Path
from starlette import status
from typing import Annotated
from concurrent.futures import ThreadPoolExecutor

from Backend.Model.request_model import Req_Collection
from Backend.Model.response_model import Res_Collection
from Backend.Model.db_model import Teacher
from Backend.Business.collection_business import collection_business
from Backend.Business.authenticate_bussiness import get_current_user

collection_router = APIRouter(prefix='/collection', tags=['collection', 'teacher'])


@collection_router.get('/', status_code=status.HTTP_200_OK, response_model=list[Res_Collection])
async def get_collections(teacher: Annotated[Teacher, Depends(get_current_user)],
                          collection_service: Annotated[collection_business, Depends()]):
    try:
        with ThreadPoolExecutor() as executor:
            return list(executor.map(lambda collection: Res_Collection(**collection), collection_service.get_collections_by_teacher(teacher.id)))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Can not get collections!")


@collection_router.get('/{collection_id}', status_code=status.HTTP_200_OK, response_model=Res_Collection)
async def get_collection(collection_id: Annotated[str, Path(min_length=8, max_length=8)],
                         collection_service: Annotated[collection_business, Depends()]):
    try:
        return collection_service.get_collection_by_id(collection_id)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Can not get collection!")


@collection_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_collection(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_Collection, Body()],
                            collection_service: Annotated[collection_business, Depends()]):
    try:
        return collection_service.insert_collection(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@collection_router.patch('/update', status_code=status.HTTP_200_OK)
async def update_collection(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_Collection, Body()],
                            collection_service: Annotated[collection_business, Depends()]):
    try:
        if data.id is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="id is required!")
        collection_service.update_collection(teacher_id=teacher.id, data=data)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
