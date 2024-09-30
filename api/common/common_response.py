from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

# 定义泛型类型，用于响应体中支持任意类型的数据
T = TypeVar('T')

class CommonResponse(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T] = None

# 成功响应
def success_response(data: Any = None, message: str = "success") -> CommonResponse:
    return CommonResponse[Any](code=0, message=message, data=data)

# 失败响应
def fail_response(message: str = "Failure", code: int = 400) -> CommonResponse:
    return CommonResponse[Any](code=code, message=message, data=None)
