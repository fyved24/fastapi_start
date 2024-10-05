from pydantic import BaseModel
from typing import Any

class Page(BaseModel):
    page: int = 1    # 页码，默认第1页
    size: int = 10   # 每页大小，默认10条
    total: int = 0   # 总数

class BaseRespSchema(BaseModel):
    page: Page = Page()
    items: list[Any]