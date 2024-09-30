from common import assert_util
from common.errs import ErrorCode
from models.user import User
from schemas.user import UserCreate, UserUpdate
from sqlmodel import Field, Session, SQLModel, create_engine, select

class UserDAL:
    def __init__(self,  session: Session):
        self.session = session

    # 创建用户
    def create_user(self, user_data: UserCreate) -> User:
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            age=user_data.age,
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user
    def all_users(self) -> list[User]:
        statement = select(User)
        results = self.session.exec(statement)
        users = results.all()
        return users

   # 获取用户通过 ID
    def get_user_by_id(self, user_id: int) -> User:
        statement = select(User).where(User.id == user_id)
        results = self.session.exec(statement)
        user = results.first()
        return user

    # 获取用户通过用户名
    def get_user_by_username(self, username: str) -> User:
        statement = select(User).where(User.name == username)
        results = self.session.exec(statement)
        user = results.one()
        return user

    def update_user(self, user_data: UserUpdate) -> User:
        user = self.get_user_by_id(user_data.id)
        assert_util.not_none(user, ErrorCode.USER_NOT_FOUND)
        if user_data.username is not None:
            user.username = user_data.username
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.password is not None:
            user.password = user_data.password
        if user_data.age is not None:
            user.age = user_data.age
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user