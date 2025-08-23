from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime


class Task(Base):
    """
    任务执行状态实体类模型
    对应数据库中的tasks表
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, comment="主键ID")
    task_id = Column(Integer, nullable=False, index=True, comment="任务ID，表示一种类型的任务")
    task_E_id = Column(String(32), nullable=False, unique=True, index=True, comment="任务执行ID，表示任务执行的唯一标识")
    status = Column(String(20), nullable=False, default="pending", comment="任务状态（pending, running, stop, finished）")
    created_time = Column(DateTime(timezone=True), server_default=func.now(), comment="任务创建时间")
    finish_time = Column(DateTime(timezone=True), nullable=True, comment="任务完成或终止时间")