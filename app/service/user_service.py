from typing import Optional
from sqlalchemy.orm import Session
from app.database.models.user import User

class UserService:
    """
    用户服务类，处理用户相关的业务逻辑
    """
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """
        根据用户ID获取用户信息
        
        Args:
            db: 数据库会话
            user_id: 用户ID
            
        Returns:
            User对象或None
        """
        return db.query(User).filter(User.id == user_id, User.is_active == True).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """
        根据用户名获取用户信息
        
        Args:
            db: 数据库会话
            username: 用户名
            
        Returns:
            User对象或None
        """
        return db.query(User).filter(User.username == username, User.is_active == True).first()
    
    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100):
        """
        获取所有用户（分页）
        
        Args:
            db: 数据库会话
            skip: 跳过的记录数
            limit: 返回的记录数
            
        Returns:
            用户列表
        """
        return db.query(User).filter(User.is_active == True).offset(skip).limit(limit).all()