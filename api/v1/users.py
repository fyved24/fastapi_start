from core.dependencies import get_db
from api.common.common_response import CommonResponse, success_response, fail_response
from fastapi import APIRouter, HTTPException, Depends

from schemas.user import UserCreate, UserRead, UserUpdate
from services.user_service import UserService
from sqlmodel import Session
router = APIRouter()

# 创建一个根据用户ID获取用户的路由
@router.get("/user/{user_id}", response_model=CommonResponse[UserRead])
async def read_user(user_id: int,  session: Session = Depends(get_db)):
    user_service = UserService(session)
    user = user_service.get_user(user_id)
    return success_response(user)

@router.get("/users", response_model=CommonResponse[list[UserRead]])
async def read_users(session: Session = Depends(get_db)):
    user_service = UserService(session)
    users = user_service.all_users()
    return success_response(users)

# 创建一个根据用户ID获取用户的路由
@router.post("/user/add", response_model=CommonResponse[UserRead])
async def read_user(user: UserCreate, session: Session = Depends(get_db)):
    user_service =  UserService(session)
    user = user_service.create_user(user)
    return success_response(user)

@router.post("/user/update", response_model=CommonResponse[UserRead])
async def read_user(user: UserUpdate, session: Session = Depends(get_db)):
    user_service =  UserService(session)
    user = user_service.update_user(user)
    return success_response(user)

