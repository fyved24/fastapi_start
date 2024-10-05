from common.errs import ErrorCode
from api.common.common_response import CommonResponse, success_response, fail_response, fail_response_with_code
from fastapi import APIRouter, Depends
from fastapi.security import  OAuth2PasswordRequestForm

from common.token_manager import get_current_user, authenticate_user, create_access_token
from dal.user_dal import UserDAL
from models.user import User, BaseUser
from schemas.req.user import UserCreate
from services.user_service import UserService

router = APIRouter()

# 创建一个根据用户ID获取用户的路由
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),  user_dal: UserDAL = Depends()):
    username = form_data.username
    password = form_data.password
    user = authenticate_user(user_dal, username, password)
    access_token = create_access_token(data={"sub": user.username})
    # 数据库验证
    if user:
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        return fail_response_with_code(ErrorCode.INVALID_CREDENTIALS)

@router.get("/me")
async def me(current_user: User = Depends(get_current_user)) -> CommonResponse[BaseUser]:
    return success_response(current_user)

@router.post("/add")
async def add(user: UserCreate, user_service: UserService = Depends()):
    user_service.create_user(user)
    return success_response()
