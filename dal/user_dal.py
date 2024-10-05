from core.dependencies import get_db
from dal import utils
from models.user import User
from sqlmodel import Session, select
from fastapi import Depends
from schemas.req.user import UserQuery


class UserDAL:
    def __init__(self,  session: Session = Depends(get_db)):
        self.session = session

    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_byid(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        results = self.session.exec(statement)
        user = results.first()
        return user

    def get_user_by_name(self, user_name: str) -> User | None:
        statement = select(User).where(User.username == user_name)
        results = self.session.exec(statement)
        user = results.first()
        return user

    def list_users(self, query_params: UserQuery) -> list[User]:
        statement = select(User)
        statement = utils.apply_sort(User, statement, query_params.sort_fields)
        statement = utils.apply_page(statement, query_params.page)
        print(str(statement))
        results = self.session.exec(statement)
        records = results.all()
        return records
