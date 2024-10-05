from models.base import BizBaseModel
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int |  None = None

class BaseUser(BaseModel):
    username: str
    email: str

class User(BaseUser, BizBaseModel, table=True):
    hashed_password: str

