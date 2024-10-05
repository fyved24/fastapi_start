from enum import Enum

class ErrorCode(Enum):
    # 50000 用户异常
    USER_NOT_FOUND = (50001, "用户不存在")
    INVALID_CREDENTIALS = (50002, "Token无效")

    # 60000 数据库异常
    INVALID_SORT_FIELD = (60001, "错误的排序字段")
    INVALID_PAGINATION =  (60001, "错误的分页")



    def __init__(self, code, message):
        self.code = code
        self.message = message
