from fastapi import FastAPI

from .request_log import RequestLogMiddleware


def register_middleware_handle(app: FastAPI):
    # 添加耗时请求中间件
    app.add_middleware(RequestLogMiddleware)