# app/core/dependencies.py
from sqlmodel import Session
from core.database import engine

# 使用 with 语句管理 SQLModel 的 Session
def get_db():
    with Session(engine) as session:
        yield session  # 将 session 提供给依赖注入
        # with 语句会在这里自动关闭 session
