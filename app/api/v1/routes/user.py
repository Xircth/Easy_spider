from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.result import ApiResponse
from app.database import get_db
from app.service.user_service import UserService
from app.core.security import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/{user_id}", response_model=dict, dependencies=[Depends(get_current_user)])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    根据用户ID获取用户信息
    
    Args:
        user_id: 用户ID
        db: 数据库会话
        current_user: 当前登录用户信息
        
    Returns:
        用户信息JSON数据
    """
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    # 将用户对象转换为字典，排除敏感信息，并处理datetime类型
    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": user.is_active,
        "is_superuser": user.is_superuser,
        "created_at": user.created_at.isoformat() if user.created_at else None,
        "updated_at": user.updated_at.isoformat() if user.updated_at else None
    }
    
    return ApiResponse.success(data=user_data, message="获取用户信息成功")