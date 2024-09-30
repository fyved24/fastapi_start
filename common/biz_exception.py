from common.errs import ErrorCode

class BizException(Exception):
    def __init__(self, error_code: ErrorCode, extra_info: str = None):
        self.error_code = error_code
        self.extra_info = extra_info
        super().__init__(self.error_code.message)

    def __str__(self):
        if self.extra_info:
            return f"{self.error_code.message} - {self.extra_info}"
        return self.error_code.message
