from fastapi import APIRouter, Depends

from api.common.common_response import CommonResponse, success_response
from common.token_manager import get_current_user
from models.user import User
from schemas.req.record import RecordQuery
from schemas.resp.record import RecordResp
from services.record_service import RecordService

router = APIRouter()

# 创建一个获取所有记录的路由
@router.post("/records")
async def read_records(
        query_params: RecordQuery,
        current_user: User = Depends(get_current_user),
        record_service: RecordService = Depends()) -> CommonResponse[RecordResp]:
    resp = record_service.fetch_data(query_params)
    return success_response(resp)
