from typing import Optional
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.ENV}/auth/login")

class UserToken(BaseModel):
    id: str
    sub: str

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserToken:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        return UserToken(id=user_id, sub=user_id)
    except JWTError:
        raise credentials_exception
