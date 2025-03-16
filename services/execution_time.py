import time
from fastapi import Request

class ExecutionTimeMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        response.headers["X-Execution-Time"] = f"{duration:.4f}s"
        return response
