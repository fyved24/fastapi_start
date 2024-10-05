from fastapi import FastAPI
from api import api_router
from api.common.exceptions_handler import register_exception_handlers
from core.database import engine
from sqlmodel import SQLModel

SQLModel.metadata.create_all(engine)
app = FastAPI()

# 注册路由
app.include_router(api_router, prefix="/api")
# 注册全局异常处理器
register_exception_handlers(app)
