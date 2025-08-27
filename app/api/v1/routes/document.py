from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.result import ApiResponse
from app.database import get_db
from app.service.document_service import DocumentService
from app.core.security import get_current_user

router = APIRouter(prefix="/doc", tags=["doc"])

@router.get("/test")
def test_endpoint():
    return ApiResponse.success("hello world wow")

@router.get("/docs", response_model=dict)
def get_all_documents(db: Session = Depends(get_db)):
    """
    查询所有文档数据
    
    Args:
        db: 数据库会话
        current_user: 当前登录用户信息
        
    Returns:
        文档数据列表的JSON响应
    """
    documents = DocumentService.get_all_documents(db)
    
    # 将Document对象列表转换为字典列表
    documents_data = [
        {
            "id": doc.id,
            "name": doc.name,
            "table_name": doc.table_name,
            "count": doc.count,
            "comment": doc.comment,
            "source": doc.source,
            "created_at": doc.created_at.isoformat() if doc.created_at else None,
            "updated_at": doc.updated_at.isoformat() if doc.updated_at else None
        }
        for doc in documents
    ]
    
    return ApiResponse.success(data=documents_data, message="获取所有文档数据成功")

@router.get("/by_source")
def get_documents_by_source(source, db: Session = Depends(get_db)):
    """
    根据任务ID查询该文档类型的信息
    
    Args:
        source: 任务ID
        db: 数据库会话
        current_user: 当前登录用户信息
        
    Returns:
        指定来源的文档数据列表的JSON响应
    """
    documents = DocumentService.get_documents_by_source(db, source)
    
    # 将Document对象列表转换为字典列表
    documents_data = [
        {
            "id": doc.id,
            "name": doc.name,
            "table_name": doc.table_name,
            "count": doc.count,
            "comment": doc.comment,
            "source": doc.source,
            "created_at": doc.created_at.isoformat() if doc.created_at else None,
            "updated_at": doc.updated_at.isoformat() if doc.updated_at else None
        }
        for doc in documents
    ]
    
    return ApiResponse.success(data=documents_data, message=f"获取任务ID为 {source} 的文档数据成功")

@router.get("/columns", response_model=dict)
def get_table_columns(table_name: str, db: Session = Depends(get_db)):
    """
    根据表名获取该数据表中的所有字段名称和属性情况
    
    Args:
        table_name: 表名
        db: 数据库会话
        current_user: 当前登录用户信息
        
    Returns:
        包含字段信息的字典列表的JSON响应
    """
    try:
        columns = DocumentService.get_table_columns(db, table_name)
        return ApiResponse.success(data=columns, message=f"获取表 {table_name} 的字段信息成功")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"获取表结构失败: {str(e)}"
        )

@router.get("/data", response_model=dict)
def get_table_data(
    table_name: str,
    columns: str = "",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    根据表名和指定字段，分页获取表中的数据
    
    Args:
        table_name: 表名
        columns: 要查询的字段列表，以逗号分隔
        skip: 跳过的记录数
        limit: 返回的记录数
        db: 数据库会话
        current_user: 当前登录用户信息
        
    Returns:
        包含分页数据的JSON响应
    """
    try:
        # 解析字段列表
        column_list = [col.strip() for col in columns.split(",")] if columns else []
        print("解析成功")
        # 如果没有指定字段，则获取所有字段
        if not column_list:
            table_columns = DocumentService.get_table_columns(db, table_name)
            column_list = [col["name"] for col in table_columns]
        
        result = DocumentService.get_table_data_paginated(db, table_name, column_list, skip, limit)
        return ApiResponse.success(data=result, message=f"获取表 {table_name} 的数据成功")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"获取表数据失败: {str(e)}"
        )
