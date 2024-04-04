import starlette.status
import fastapi
from typing import Annotated
from jose import jwt, JWTError
from datetime import datetime, timedelta
from ..Model.db_model import Teacher, Student
from . import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, HASH_ALGORITHM, oauth2_scheme


def create_access_token(data: dict, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    encode = data.copy()
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=HASH_ALGORITHM)


async def get_current_user(token: Annotated[str, fastapi.Depends(oauth2_scheme)]):
    credentials_exception = fastapi.HTTPException(
        status_code=starlette.status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASH_ALGORITHM])
        role = payload.get("role")
        if role == "teacher":
            return Teacher({'id': payload.get('id'), 'email': payload.get('email')})
        elif role == "student":
            return Student({'id': payload.get('id'), 'email': payload.get('email')})
        elif role == "admin":
            pass
        else:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
