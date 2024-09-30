from fastapi import APIRouter, HTTPException

router = APIRouter()

# 创建一个获取所有记录的路由
@router.get("/records/")
async def read_records():
    return [{"record_id": 1, "data": "Record 1"}, {"record_id": 2, "data": "Record 2"}]

# 创建一个根据记录ID获取记录的路由
@router.get("/records/{record_id}")
async def read_record(record_id: int):
    if record_id == 1:
        return {"record_id": 1, "data": "Record 1"}
    elif record_id == 2:
        return {"record_id": 2, "data": "Record 2"}
    raise HTTPException(status_code=404, detail="Record not found")
