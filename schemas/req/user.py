from datetime import datetime

from pydantic import BaseModel

from models.user import BaseUser
from schemas.common.base_query_schema import BaseQuerySchema


class UserQuery(BaseQuerySchema):
    username: str

class UserCreate(BaseUser):
    password: str
