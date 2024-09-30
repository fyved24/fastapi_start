from pydantic import BaseModel

# 创建用户时使用的 Pydantic 模型
class UserCreate(BaseModel):
    username: str
    email: str
    password: str  # 明文密码，用于输入
    age: int

# 返回用户信息时使用的 Pydantic 模型
class UserRead(BaseModel):
    id: int
    username: str
    email: str
    age: int

# 更新用户信息时使用的 Pydantic 模型
class UserUpdate(BaseModel):
    id: int
    username: str | None
    email: str | None
    password: str | None
    age: int| None
