from common.biz_exception import BizException
from common.errs import ErrorCode


def is_true(result: bool, err_code: ErrorCode):
    if result is not True:
        raise BizException(err_code)


def is_false(result: bool, err_code: ErrorCode):
    if result is not False:
        raise BizException(err_code)

def not_none(result: object, err_code: ErrorCode):
    if result is None:
        raise BizException(err_code)