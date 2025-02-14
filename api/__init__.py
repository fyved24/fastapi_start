from api.v1 import api_router as v1

from fastapi import APIRouter

api_router = APIRouter()

# 绑定 users 模块的路由
api_router.include_router(v1, prefix="/v1", tags=["v1"])