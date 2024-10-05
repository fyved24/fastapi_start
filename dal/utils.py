from common.biz_exception import BizException
from common.errs import ErrorCode
from schemas.common.base_query_schema import SortField, Page
from typing import Any


def apply_sort(schema: Any, statement, sort_fields: list[SortField]):
    for sort in sort_fields:
        try:
            field = getattr(schema, sort.field)
            print(field)
        except AttributeError as e:
            raise BizException(ErrorCode.INVALID_SORT_FIELD, extra_info=str(e))
        if sort.order == "asc":
            statement = statement.order_by(field.asc())
        else:
            statement = statement.order_by(field.desc())
    return statement

def apply_page(statement, page: Page):
    try:
        # 计算偏移量 (offset) 和每页记录数 (limit)
        offset = (page.page - 1) * page.size
        limit = page.size
        print(offset)
        print(limit)
        # 应用 offset 和 limit
        statement = statement.offset(offset).limit(limit)
    except Exception as e:
        raise BizException(ErrorCode.INVALID_PAGINATION, extra_info=str(e))
    return statement