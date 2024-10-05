from fastapi import  Depends

from common.token_manager import get_password_hash
from dal.user_dal import UserDAL
from models.user import User
from schemas.req.user import UserCreate


class UserService:
    def __init__(self, user_dal: UserDAL = Depends()):
        self.user_dal = user_dal

    def create_user(self, base_user: UserCreate) -> User:
        user = User(**base_user.model_dump(exclude={"password"}))
        hashed_password = get_password_hash(base_user.password)
        user.hashed_password = hashed_password
        self.user_dal.create_user(user)
        return user