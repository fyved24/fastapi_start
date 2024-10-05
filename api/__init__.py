from sys import prefix

from fastapi import APIRouter
from api import record, user

# 创建一个 APIRouter 实例来包含所有的路由模块
api_router = APIRouter()

# 绑定 users 模块的路由
api_router.include_router(user.router, prefix="/user", tags=["users"])

# 绑定 records 模块的路由
api_router.include_router(record.router, prefix="/record", tags=["record"])
