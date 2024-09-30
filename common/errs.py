from enum import Enum

class ErrorCode(Enum):
    USER_NOT_FOUND = (50001, "User not found")
    INVALID_CREDENTIALS = (50002, "Invalid username or password")

    def __init__(self, code, message):
        self.code = code
        self.message = message
