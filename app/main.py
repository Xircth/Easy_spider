from fastapi import FastAPI, Depends
from app.api.v1.api import api_router
from app.utils.result import ApiResponse
# from app.core.exceptions import setup_exception_handlers
from app.database import engine, Base
from sqlalchemy import text
from app.database import get_db
from app.core.security import JWTBearer, get_current_user

app = FastAPI(title="Pulgin_Project", version="1.0.0")

# 使用正确的全局认证配置方式
app = FastAPI(
    title="Pulgin_Project",
    version="1.0.0"
)

# 创建数据库表
Base.metadata.create_all(bind=engine)

# # 注册异常处理器
# setup_exception_handlers(app)
@app.on_event("startup")
async def startup_event():
    """
    应用启动时的事件处理
    可以在这里进行数据库连接测试等初始化操作
    """
    # 测试数据库连接
    try:
        db = next(get_db())
        db.execute(text("SELECT 1"))
        print("数据库连接成功")
    except Exception as e:
        print(f"数据库连接失败: {e}")
        raise

# 包含 API 路由
# app.include_router(api_router, prefix="/api/v1")
app.include_router(api_router)

@app.get("/")
def read_root():
    return ApiResponse.success("hello")


