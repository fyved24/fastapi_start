# app/services/user_service.py

from sqlmodel import Session

from common import assert_util
from common.errs import ErrorCode
from schemas.user import UserCreate, UserUpdate
from dal.user_dal import UserDAL

class UserService:
    def __init__(self, session: Session):
        self.user_dal = UserDAL(session)

    def create_user(self, user_data: UserCreate):
        return self.user_dal.create_user(user_data)

    def get_user(self, user_id: int):
        user = self.user_dal.get_user_by_id(user_id)
        assert_util.not_none(user, ErrorCode.USER_NOT_FOUND)
        return user

    def all_users(self):
        return self.user_dal.all_users()

    def update_user(self, user_data: UserUpdate):
        return self.user_dal.update_user(user_data)
