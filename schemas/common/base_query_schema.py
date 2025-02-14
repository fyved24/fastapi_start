from pydantic import BaseModel


class SortField(BaseModel):
    field: str                    # 排序字段名称
    order: str = "asc"   #

class Page(BaseModel):
    pageSize: int
    currentPage: int

class BaseQuerySchema(BaseModel):
    pass

class BasePagedQuerySchema(BaseQuerySchema):
    sort_fields: list[SortField] # 排序字段列表
    page: Page