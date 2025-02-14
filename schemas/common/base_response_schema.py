from pydantic import BaseModel
from typing import Any

class Page(BaseModel):
    pageSize: int = 1    # 页码，默认第1页
    currentPage: int = 10   # 每页大小，默认10条
    total: int = 0   # 总数

class BaseRespSchema(BaseModel):
    pass

class BasePagedRespSchema(BaseRespSchema):
    page: Page = Page()