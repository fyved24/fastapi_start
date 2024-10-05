from enum import Enum

class Operator(Enum):
    eq = "eq"    # 等于
    lt = "lt"    # 小于
    gt = "gt"    # 大于
    lte = "le"  # 小于等于
    gte = "ge"  # 大于等于
    ne = "ne"    # 不等于
