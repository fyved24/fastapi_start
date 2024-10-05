from pydantic import BaseModel


class SortField(BaseModel):
    field: str                    # 排序字段名称
    order: str = "asc"   #

class Page(BaseModel):
    page: int = 1 # 页码，默认第1页
    size: int = 10# 每页大小，默认10条

class BaseQuerySchema(BaseModel):
    sort_fields: list[SortField] = []  # 排序字段列表
    page: Page = Page()