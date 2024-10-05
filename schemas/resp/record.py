from datetime import datetime

from models.record import Record
from schemas.common.base_response_schema import BaseRespSchema

class RecordResp(BaseRespSchema):
    items: list[Record]

