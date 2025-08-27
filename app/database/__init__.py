from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils.config_init import get_config

# 获取数据库配置
mysql_config = get_config("mysql_config")

# 构建数据库连接URL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{mysql_config['username']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}"

# 创建数据库引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # 开启连接健康检查
    pool_recycle=3600,   # 每小时自动回收连接
)

# 创建SessionLocal类
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

# 创建Base类
Base = declarative_base()

def get_db():
    """
    获取数据库会话
    用于FastAPI的依赖注入
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()