import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class RequestLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        # 读取请求体数据（bytes类型）
        request_body = await request.body()
        # 打印请求体内容（假设是UTF-8编码）
        print("Request:", request_body.decode("utf-8") if request_body else "")

        # 由于请求体只能读取一次，因此需要重置 request._receive
        async def receive():
            return {"type": "http.request", "body": request_body}

        request._receive = receive

        start_time = time.time()
        # 调用下一个中间件或路由处理函数
        response = await call_next(request)

        # 捕获响应体数据
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk
        # 打印响应体内容
        print("Response:", response_body.decode("utf-8") if response_body else "Empty")

        process_time = time.time() - start_time
        print(f"Cost: {process_time:.4f}s")

        # 由于 response.body_iterator 已经被消费，重新构造一个 Response 返回
        new_response = Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
        return new_response
