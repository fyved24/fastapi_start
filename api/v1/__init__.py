from fastapi import APIRouter
from api.v1 import users, records

# 创建一个 APIRouter 实例来包含所有的路由模块
api_router = APIRouter()

# 绑定 users 模块的路由
api_router.include_router(users.router, prefix="/v1", tags=["users"])

# 绑定 records 模块的路由
api_router.include_router(records.router, prefix="/v1", tags=["records"])
