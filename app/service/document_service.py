from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.database.models.document import Document


class DocumentService:
    """
    文档服务类，处理文档相关的业务逻辑
    """
    
    @staticmethod
    def get_all_documents(db: Session) -> List[Document]:
        """
        查询所有文档数据
        
        Args:
            db: 数据库会话
            
        Returns:
            Document对象列表
        """
        return db.query(Document).all()
    
    @staticmethod
    def get_documents_by_source(db: Session, source: int) -> List[Document]:
        """
        根据任务ID（即其中的source字段）获取该文档类型的所有数据
        
        Args:
            db: 数据库会话
            source: 任务ID
            
        Returns:
            Document对象列表
        """
        return db.query(Document).filter(Document.source == source).all()
    
    @staticmethod
    def get_table_columns(db: Session, table_name: str) -> List[Dict[str, Any]]:
        """
        根据表名获取该数据表中的所有字段名称和属性情况
        
        Args:
            db: 数据库会话
            table_name: 表名
            
        Returns:
            包含字段信息的字典列表
        """
        # 使用反射获取表信息
        from sqlalchemy import inspect
        inspector = inspect(db.bind)
        
        # 获取表的所有列信息
        columns = inspector.get_columns(table_name)
        
        # 提取需要的字段信息
        result = []
        for column in columns:
            column_info = {
                "name": column["name"],
                "type": str(column["type"]),
                "nullable": column["nullable"],
                "default": column["default"],
                "comment": column.get("comment", "")
            }
            result.append(column_info)
        
        return result
    
    @staticmethod
    def get_table_data_paginated(db: Session, table_name: str, columns: List[str],
                               skip: int = 0, limit: int = 100) -> Dict[str, Any]:
        """
        根据表名和指定字段，分页获取表中的数据
        
        Args:
            db: 数据库会话
            table_name: 表名
            columns: 要查询的字段列表
            skip: 跳过的记录数
            limit: 返回的记录数
            
        Returns:
            包含分页数据和总数的字典
        """
        # 动态创建表对象
        from sqlalchemy import Table, MetaData
        metadata = MetaData()
        table = Table(table_name, metadata, autoload_with=db.bind)
        
        # 构建查询，只选择指定的列
        query = db.query(*[table.c[col] for col in columns])
        
        # 获取总数
        total = query.count()
        
        # 执行分页查询
        results = query.offset(skip).limit(limit).all()
        
        # 转换为字典列表
        data = []
        for row in results:
            row_dict = {}
            for col in columns:
                row_dict[col] = getattr(row, col)
            data.append(row_dict)
        
        return {
            "data": data,
            "total": total,
            "skip": skip,
            "limit": limit
        }