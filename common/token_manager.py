from fastapi import HTTPException, Depends, status
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError

import jwt

from common.errs import ErrorCode
from core.security import pwd_context, oauth2_scheme
from common import assert_util, errs
from dal.user_dal import UserDAL
from models.user import User
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(user_dal: UserDAL, username: str)->User:
    user = user_dal.get_user_by_name(username)
    assert_util.not_none(user, errs.ErrorCode.USER_NOT_FOUND)
    return user


def authenticate_user(db, username: str, password: str)->User | None:
    user = get_user(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str =  Depends(oauth2_scheme), user_dal: UserDAL = Depends()):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except InvalidTokenError:
        username = None
    assert_util.not_none(username, ErrorCode.INVALID_CREDENTIALS)
    user = get_user(user_dal, username=username)
    return user

