from fastapi import FastAPI
from app.api.v1.api import api_router
from app.utils.result import ApiResponse
# from app.core.exceptions import setup_exception_handlers

app = FastAPI(title="Pulgin_Project", version="1.0.0")

# # 注册异常处理器
# setup_exception_handlers(app)

# 包含 API 路由
# app.include_router(api_router, prefix="/api/v1")
app.include_router(api_router)

@app.get("/")   
def read_root():
    return ApiResponse.success("hello")

