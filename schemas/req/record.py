from datetime import datetime

from pydantic import BaseModel

from schemas.common.base_query_schema import BaseQuerySchema

class RecordQuery(BaseQuerySchema):
    begin_time: datetime | None = None
    end_time: datetime | None = None
