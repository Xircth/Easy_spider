from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Document(Base):
    """
    文档实体类模型
    对应数据库中的document表
    用于存储任务采集到的数据的汇总管理
    """
    __tablename__ = "document"

    id = Column(Integer, primary_key=True, index=True, comment="主键ID")
    name = Column(String(100), nullable=False, comment="采集表名字")
    table_name = Column(String(100), nullable=False, unique=True, index=True, comment="数据存储表名")
    count = Column(BigInteger, nullable=False, default=0, comment="采集数据总数")
    comment = Column(Text, comment="备注")
    source = Column(Integer, nullable=False, index=True, comment="任务来源（任务ID）")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="更新时间")