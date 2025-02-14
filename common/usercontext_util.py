import contextvars

from models.user import BaseUser

# 定义一个 context variable 用于存储当前登录用户信息，默认值为 None
_current_user = contextvars.ContextVar("current_user", default=None)

def set_current_user(user):
    """设置当前登录用户，并返回 token 以便后续重置"""
    return _current_user.set(user)

def get_current_user():
    """获取当前登录用户"""
    return _current_user.get()

def reset_current_user(token):
    """根据 token 重置当前登录用户"""
    _current_user.reset(token)