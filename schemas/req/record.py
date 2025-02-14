from datetime import datetime

from pydantic import BaseModel

from schemas.common.base_query_schema import BaseQuerySchema, BasePagedQuerySchema


class RecordQuery(BasePagedQuerySchema):
    begin_time: datetime | None = None
    end_time: datetime | None = None
